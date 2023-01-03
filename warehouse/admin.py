from django.contrib import admin
from .models import Category, Product
# Register your models here.

m = [Category, Product,]

for i in m:
    admin.site.register(i)