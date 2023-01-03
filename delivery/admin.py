from django.contrib import admin
from .models import DeliveryRider, DeliveryCompany
# Register your models here.

m = [ DeliveryRider, DeliveryCompany ]

for i in m:
    admin.site.register(i)