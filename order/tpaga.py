from base64 import b64encode
from datetime import datetime, timedelta
from django.conf import settings
from order.models import Order, OrderProduct
from uuid import uuid4
import requests
import json

def getAuthorization():
    authorization = ("{0}:{1}".format(settings.TPAGA_USERNAME, settings.TPAGA_PASSWORD)).encode()
    return b64encode(authorization).decode()

def createPayRequest(order, purchase_details_url):
    orderProducts = OrderProduct.objects.filter(order=order)
    purchase_items = []
    for product in orderProducts:
        purchase_items.append({
            "name": product.product.name,
            "value": product.total
        })
    expire_date = datetime.now() + timedelta(minutes=30)

    data = {
        "cost": order.total,
        "purchase_details_url": purchase_details_url,
        "idempotency_token":str(uuid4()),
        "order_id":order.id,
        "terminal_id":"minitrade",
        "purchase_description":order.details,
        "purchase_items": purchase_items,
        "user_ip_address":order.client,
        "expires_at": expire_date.astimezone().isoformat()
    }
    # print(data)
    response = requests.post('https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/create',
        data= json.dumps(data), headers={
            "Content-Type" : "application/json",
            "Cache-Control": "no-cache",
            "authorization" : "Basic "+ getAuthorization()})
    # print(response.json())
    if response.status_code == 201:
        data = response.json()
        return {
            "token": data["token"],
            "url": data["tpaga_payment_url"],
            "status": data["status"]
        }
    else:
        return {
            "token": "",
            "url": "",
            "status": "failed"
        }

def confirmStateTransaction(token):
    response = requests.get('https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/'+token+'/info',
        headers={
            "Content-Type" : "application/json",
            "Cache-Control": "no-cache",
            "authorization" : "Basic "+ getAuthorization()})

    if response.status_code == 201:
        data = response.json()
        return {
            "status": data["status"]
        }
    else:
        return {
            "token": "",
            "url": "",
            "status": "failed"
        }

def revertedPaid(token):
    response = requests.post('https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/refund',
        data=json.dumps({"payment_request_token": token}), headers={
            "Content-Type" : "application/json",
            "Cache-Control": "no-cache",
            "authorization" : "Basic "+ getAuthorization()})

    data = response.json()
    # print(data)
    return data.get('status') == 'reverted'