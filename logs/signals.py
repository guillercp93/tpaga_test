from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.models import Order
from logs.models import Log

@receiver(pre_save, sender=Order)
def createRegister(sender, instance, **kwargs):
    try:
        old = sender.objects.get(id=instance.id)
        oldstatus = old.status
    except:
        oldstatus = None
    if oldstatus != instance.status:    
        log = Log()
        log.order = instance
        log.status = instance.status
        log.save()