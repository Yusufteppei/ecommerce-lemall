from django.db import models
from address.models import Locality, State, Address
#from orders.models import ReceivedOrder

#   THE PACKAGE IS GIVEN TO A DELIVERY COMPANY
#   A DELIVERY RIDER AUTHENTICATION SYSTEM IS REQUIRED
#   THE DELIVERY COMPANIES SHOULD PLACE THEIR DELIVERY BID AND THE SYSTEM WILL PICK THE BEST FOR A DELIVERY
#   PERHAPS THE BUYERS SHOULD PICK A DELIVERY AFTER SEEING THE OPTIONS
# 
#  

class DeliveryCompany(models.Model):
    name = models.CharField(max_length=64)
    states = models.ManyToManyField(State)
    locations = models.ManyToManyField(Address)
    deliverable_regions = models.ManyToManyField(Locality)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Delivery Companies'


class DeliveryRider(models.Model):
    full_name = models.CharField(max_length=64)
    delivery_company = models.ForeignKey(DeliveryCompany, on_delete=models.CASCADE, null=True, blank=True)# DEFAULT IS LEMALL DELIVERY
    regions = models.ManyToManyField(Locality)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name_plural = 'Delivery Riders'


class Package(models.Model):
    #order = models.ForeignKey(ReceivedOrder, on_delete=models.PROTECT)
    delivery_rider = models.ForeignKey(DeliveryRider, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.order}-{self.delivery_rider}-{self.id}'

