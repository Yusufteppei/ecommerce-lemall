from rest_framework.serializers import ModelSerializer
from .models import Wishlist, WishlistItem, Cart, CartItem, Order, Profile
from rest_framework import serializers

class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

    
class WishlistItemSerializer(ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = '__all__'


class CartItemSerializer(ModelSerializer):
    product = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = '__all__'



class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

