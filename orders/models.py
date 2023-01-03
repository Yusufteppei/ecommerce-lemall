from django.db import models
from delivery.models import DeliveryRider
from address.models import Address
from userapp.models import Order


class ReceivedOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivery_rider = models.ForeignKey(DeliveryRider, on_delete=models.PROTECT, blank=True, null=True)
    # deliver_company = models.ForeignKey(DeliveryCompany, on_delete=models.PROTECT)

    check_out_date = models.DateTimeField(auto_now_add=True, editable=False)
    processed = models.BooleanField(default=False)
    on_transit = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    delivery_address = models.ForeignKey(Address, on_delete=models.PROTECT, blank=True, null=True)# CONTACT APP

    def __str__(self) -> str:
        return f"Received Order {self.id}-{self.order.id}"

    class Meta:
        verbose_name_plural = 'Received Orders'
