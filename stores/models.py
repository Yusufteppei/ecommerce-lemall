from django.db import models
from address.models import Locality, Country
from django.contrib.auth import get_user_model

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


class Store(models.Model):
    name = models.CharField(max_length=64, unique=True)
    international = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    address = models.TextField(max_length=256)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class Image(models.Model):
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
    price = models.DecimalField(decimal_places=2, max_digits=16)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True) # MAKE DEFAULT STORE
    location = models.ForeignKey(Locality, on_delete=models.CASCADE, null=True) #FIX IN PRODUCTION
    #store

    selling_price = models.IntegerField(verbose_name='Price(In Naira)', default=0)
    cost_price = models.IntegerField(blank=True, null=True)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.title

