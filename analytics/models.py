from django.db import models
from stores.models import Product
from userapp.models import Profile


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) # SET AS NAME OR DISALLOW DELETE
    time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True) #  SET AS NAME OR DISALLOW DELETE


class Refund(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) # SET AS NAME OR DISALLOW DELETE
    time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True) #  SET AS NAME OR DISALLOW DELETE
