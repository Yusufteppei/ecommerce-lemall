from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from userapp.serializers import CartItemSerializer, CartSerializer, OrderSerializer, ProfileSerializer, WishlistItemSerializer, WishlistSerializer
from .models import Wishlist, WishlistItem, Cart, CartItem, Order, Profile
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import get_user_model

from .permissions import IsOwner

# Create your views here.
User = get_user_model()

#######          WISHLIST       #########
class WishlistViewSet(ModelViewSet):
    permission_classes = [IsOwner, IsAdminUser]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return Wishlist.objects.get(owner=self.request.user)


class WishlistItemViewSet(ModelViewSet):
    permission_classes = [IsOwner, IsAdminUser]
    serializer_class = WishlistItemSerializer

    def get_queryset(self):
        return WishlistItem.objects.filter(owner=self.request.user)

#######          WISHLIST END      #########



#######          CART      #########
class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)

class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(owner=self.request.user)

def checkout(request):
    cart = Cart.objects.get(owner=request.user)
    cart.is_checked_out = True
    cart.save()
#######          CART END     #########



#######          ORDER      #########
class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)

#######          ORDER END    #########

class ProfileViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.get(owner=self.request.user)
