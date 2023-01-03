from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import ReceivedOrder
from userapp.models import Order


@receiver(post_save, sender=Order)
def create_received_order(sender, instance, created, **kwargs):
    if created:
        ReceivedOrder.objects.create(order=instance)
        print('Order Received!')
