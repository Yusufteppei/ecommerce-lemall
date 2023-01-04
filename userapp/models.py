from django.db import models
from authentication.models import UserAccount
from warehouse.models import Product
from address.models import Address
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)


class WishlistItem(models.Model):
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Wishlist(models.Model):
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE,)
    items = models.ManyToManyField(WishlistItem)

    @property
    def is_empty(self, request):
        return self.items.filter(owner_id=request).count() == 0

    @property
    def total(self):
        return self.items.a

    def __str__(self):
        return f"{self.owner}{self.id}"
    
    @property
    def no_of_items(self):
        return self.items.count()


class CartItem(models.Model):
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)

    
    def increment(self):
        self.quantity += 1
        self.save()
        return self.quantity
        
    def decrement(self):
        self.quantity -= 1
        self.save()
        return self.quantity
        
    def remove(self):
        self.delete()

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    owner = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)

    is_empty = models.BooleanField(default=True)
    is_checked_out = models.BooleanField(default=False)

    items_total_cost = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    total_tax = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    def empty_cart(self):
        self.items.objects.all().delete()

    def check_out(self):
        # self.is_checked_out = True
        pass

    def __str__(self):
        return f"{self.owner}'s Cart"


# ONCE A CART IS CHECKED OUT, THE ITEMS PAID FOR WILL BE PARSED INTO AN ORDER AND THE CART WILL BE EMPTIED
class Order(models.Model):
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    items = models.ManyToManyField(CartItem)

    partially_delivered = models.BooleanField(default=False)
    fully_delivered = models.BooleanField(default=False)

    on_transit = models.BooleanField(default=False)

    items_total_cost = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    total_tax = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    total = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    #delivery_address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, blank=True)# CONTACT APP    
    #   delivery_contact = models.ForeignKey(Address, on_delete=models.PROTECT, default='')# CONTACT APP

    def __str__(self):
        return f"Order {self.owner.id}-{self.id}"
    def cancel_order(self):
        #   cancel order
        pass

    def get_order_status(self):
        if self.partially_delivered:
            return 'Partially Delivered'

        elif self.fully_delivered:
            return 'Fully Delivered'
        pass

    def set_order_status(self, transit, partial, full):
        pass

    #def total(self):
    #    pass


#class Fingerprint(models.Model):
 #   user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
  #  liked_products = models.ManyToManyField(Product)
   # viewed_products = models.ManyToManyField(Product)
    #wishlisted_items = models.ManyToManyField(Product)
    #carted_items = models.ManyToManyField(Product)