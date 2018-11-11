from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from logs.models import Log

@receiver(post_save, sender=Order)
def createRegister(sender, instance, **kwargs):
    log = Log()
    log.order = instance
    log.status = instance.status
    log.save()