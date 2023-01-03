from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from userapp.permissions import IsAdminUserOrReadOnly

from rest_framework.decorators import action

# Create your views here.

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(active=True)
    permission_classes = [AllowAny]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminUserOrReadOnly,]


