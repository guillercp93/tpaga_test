from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.models import Order
from order.tpaga import revertedPaid

@receiver(pre_save, sender=Order)
def changeReverted(sender, instance, **kwargs):
    try:
        old = sender.objects.get(id=instance.id)
        status = old.status
    except:
        status = 'created'
        
    if instance.status == 'reverted':
        isSuccess = revertedPaid(instance.token)
        if not isSuccess:
            instance.status = status
            instance.save()
