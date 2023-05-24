from address.models import Locality
from django.db import models
from stores.models import Product

#  MODELS
class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural='Categories'



class Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.product.title}' 

    def sell(self):
        self.product.sell()