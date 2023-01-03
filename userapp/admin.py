from django.contrib import admin
from .models import Cart, CartItem, Wishlist, WishlistItem, Profile, Order

m = [Cart, Order, CartItem, Wishlist, WishlistItem, Profile]
# Register your models here.

for i in m:
    admin.site.register(i)
