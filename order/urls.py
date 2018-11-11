from order import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', views.list, name="product_list"),
    url(r'^buy_product/(?P<product_id>\d+)/$', views.buyProduct),
    url(r'^finish_buy/(?P<order_id>\d+)/$', views.finishBuy),
]
