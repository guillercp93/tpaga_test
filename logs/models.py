from django.db import models
from order.models import Order

class Log(models.Model):
    author = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    date_at = models.DateTimeField(auto_now_add=True)