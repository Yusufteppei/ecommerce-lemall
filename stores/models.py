from django.db import models
from address.models import Locality, Country
from django.contrib.auth import get_user_model
#from analytics.models import Sale, Refund
from datetime import datetime
#from userapp.models import Profile

import pandas as pd

User = get_user_model()

#  OPTIONS
STATUSES = (
    ('Pending', 'pending'),
    ('Approved', 'approved'),
    ('Rejected', 'rejected')
)


class Tag(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

#  MODELS
class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class DiscountPolicy(models.Model):
    pass


class Store(models.Model):
    name = models.CharField(max_length=64, unique=True)
    international = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=256)
    discount_policy = models.ForeignKey(DiscountPolicy, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    address = models.TextField(max_length=256)
    store = models.OneToOneField(Store, related_name='contact', on_delete=models.CASCADE)


class Image(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='store_product_images')

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return self.image.url


class Product(models.Model):
    title = models.CharField(max_length=128)
    product_type = models.CharField(max_length=64, null=True, blank=True)
    quantity = models.IntegerField()
    selling_price = models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Selling Price(In Naira)')
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True) # MAKE DEFAULT STORE
    location = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True) #FIX IN PRODUCTION
    

    #selling_price = models.IntegerField(verbose_name='Selling Price(In Naira)', default=0)
    cost_price = models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Cost Price(In Naira)', null=True, blank=True)
    images = models.ManyToManyField(Image)

    #warehouse_products = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def set_inactive(self):
        self.active = False

    def set_active(self):
        self.active = True

    def decrement_stock(self):
        self.quantity -= 1
    
    def decrement_stock(self, q):
        self.quantity -= q
    
    def increment_stock(self):
        self.quantity += 1
    
    def increment_stock(self, q):
        self.quantity += q

    def sell(self, quantity, buyer):
        self.decrement_stock(quantity)

        #  STORE DATA INTO CSV FILE
        store = self.store
        sales = pd.read_csv('Stores.csv')
        row = {
            'Store Name': store.name, 'Store Id': store.id,
         'Product Title': self.title, 'Product Id': self.id,
         'Quantity': self.quantity, 'Cost Price': self.cost_price,
         'Selling Price': self.selling_price
        }
        
        sales.append(row)
        #Sale.objects.create(product=self, time=datetime.now, quantity=quantity, buyer=buyer)

    def refund(self, quantity, buyer):
        self.increment_stock(quantity)
        #Sale.objects.delete(product=self, time=datetime.now, quantity=quantity)
        #Refund.objects.create(product=self, time=datetime.now, quantity=quantity, buyer=buyer)


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    store_name = models.CharField(max_length=64, null=True)
    store_address = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=16)

    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) # SET AS NAME OR DISALLOW DELETE
    time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True) #  SET AS NAME OR DISALLOW DELETE


"""
class Refund(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True) # SET AS NAME OR DISALLOW DELETE
    time = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    buyer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True) #  SET AS NAME OR DISALLOW DELETE
"""