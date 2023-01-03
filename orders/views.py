from orders.serializers import OrderSerializers
from .models import Order, Cart, CartItem
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OrderSerializer, CartItemSerializer, CartSerializer
from rest_framework import generics


class OrderViewset(ModelViewSet):
    query_set = Order.objects.all()
    permission_classes = ('IsAdminUser', )
    serializer_class = OrderSerializer


class CartViewset(ModelViewSet):
    query_set = Cart.objects.all()
    permission_classes = ('IsAdminUser', )
    serializer_class = CartSerializer


class CartItemViewset(ModelViewSet):
    query_set = CartItem.objects.all()
    permission_classes = ('IsAdminUser', )
    serializer_class = CartItemSerializer





# ORDERS ARE CHECKED OUT CARTS I.E PAID FOR
@api_view('GET')
def get_fresh_orders(request):
    orders = Order.objects.filter(processed=False)
    return orders


# UNATTENDED ORDERS ARE ORDERS PAID FOR BUT NOT YET HANDED TO THE DELIVERY RIDERS
@api_view('GET')
def get_unattended_orders(request):
    orders = Order.objects.filter(on_transit=False).filter(delivered=False)
    return orders


#ORDERS IN TRANSIT ARE ORDERS HANDED OVER TO THE DELIVERY RIDER
@api_view('GET')
def get_transit_orders(request):
    orders = Order.objects.filter(on_transit=True).filter(delivered=False)
    return orders


# DELIVERED ORDERS ARE ORDERS ACKNOWLEDGED BY CUSTOMERS AS DELIVERED
@api_view('GET')
def get_delivered_orders(request):
    orders = Order.objects.filter(delivered=True)
    return orders
