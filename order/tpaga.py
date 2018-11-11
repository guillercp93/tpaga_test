from uuid import uuid4
from order.models import Order, OrderProduct
from datetime import datetime, timedelta
from base64 import b64encode
import requests
import json

username="miniapp-gato1"
password="miniappma-123"

def getAuthorization():
    authorization = ("{0}:{1}".format(username, password)).encode()
    return b64encode(authorization).decode()

def createPayRequest(order):
    orderProducts = OrderProduct.objects.filter(order=order)
    purchase_items = []
    for product in orderProducts:
        purchase_items.append({
            "name": product.product.name,
            "value": product.total
        })
    expire_date = datetime.now() + timedelta(minutes=5)

    data = {
        "cost": order.total,
        "purchase_details_url": "https://example.com/compra/348820",
        "idempotency_token":str(uuid4()),
        "order_id":order.id,
        "terminal_id":"minitrade",
        "purchase_description":order.details,
        "purchase_items": purchase_items,
        "user_ip_address":order.client,
        "expires_at": expire_date.astimezone().isoformat()
    }

    response = requests.post('https://stag.wallet.tpaga.co/merchants/api/v1/payment_requests/create',
        data= json.dumps(data), headers={
            "Content-Type" : "application/json",
            "Cache-Control": "no-cache",
            "authorization" : "Basic "+ getAuthorization()})

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
