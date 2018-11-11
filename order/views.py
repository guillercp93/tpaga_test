from django.http import HttpResponse
from django.shortcuts import render
from order.models import Order, OrderProduct, Product
from order.tpaga import createRequest
import json

def list(request):
    products = Product.objects.values('id', 'name', 'details', 'price', 'trademark')
    return render(request, 'index.html', {'products': products})

def buyProduct(request, id):
    amount = request.POST.get('amount', 1)
    try:
        product = Product.objects.get(id=id)
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

        response = createRequest(order)
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