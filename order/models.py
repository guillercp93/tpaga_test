from django.db import models

class Order(models.Model):
    client = models.CharField(max_length=15)
    details = models.TextField(blank=True)
    purchased_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
    total = models.IntegerField(default=0)
    token = models.TextField(default=None, null=True)

class Product(models.Model):
    name = models.CharField(max_length=50)
    details = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    trademark = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    total = models.IntegerField(default=0)