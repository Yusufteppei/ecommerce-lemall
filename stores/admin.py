from django.contrib import admin
from .models import Store, Contact, Product, Category, Image
# Register your models here.

m = [ Store, Contact, Product, Category, Image ]

for i in m:
    admin.site.register(i)