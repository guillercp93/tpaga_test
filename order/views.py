from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from order.models import Order, OrderProduct, Product
from order.tpaga import createPayRequest, confirmStateTransaction
import json

def list(request):
    products = Product.objects.values('id', 'name', 'details', 'price', 'trademark')
    return render(request, 'items.html', {'products': products})

def buyProduct(request, product_id):
    amount = request.POST.get('amount', 1)

    try:
        product = Product.objects.get(id=product_id)
        order = Order()
        order.client = request.META["REMOTE_ADDR"]
        order.details = "is buying the product " + product.name + " in MINITRADE"
        order.total = product.price * int(amount)
        order.status = "created"
        order.save()

        orderProduct = OrderProduct()
        orderProduct.product = product
        orderProduct.order = order
        orderProduct.amount = amount
        orderProduct.total = product.price * int(amount)
        orderProduct.save()

        callback_url = "https://{0}/finish_buy/{1}/".format(request.get_host(), order.id)
        response = createPayRequest(order, callback_url)
        order.token = response['token']
        order.status = response['status']
        order.save()

        return HttpResponse(json.dumps({
            "url": response['url'] 
        }), status=200)
    except Exception as e:
        return HttpResponse(json.dumps({
            "error": str(e),
            "message": "The transaction could not be created!"
        }), status=500)

def finishBuy(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        response = confirmStateTransaction(order.token)
        order.status = response["status"]
        order.save()

        if response["status"] == "failed":
            context = {
                "status": "failed",
                "message": "We are sorry. We were not able to confirm the payment of the order no. "+ order.id + ": " + order.details
            }
        else:
            context = {
                "status": "success",
                "message": "The payment for purchase order number {0} has been validated correctly.".format(order.id)
            }

        return render(request, 'finish.html', context)
    except:
        return render(request, 'finish.html', {
            "status": "fail",
            "message": "We are sorry. The transaction has not been completed"
        })