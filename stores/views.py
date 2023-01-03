from .serializers import CategorySerializer, ProductSerializer, StoreSerializer, ContactSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from userapp.permissions import IsOwner
from .models import Product, Store, Contact, Category, Tag


class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [ permissions.AllowAny]
    queryset = Category.objects.all()


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [ permissions.AllowAny ] # RESTRICT TO OWNER
    queryset = Product.objects.all()

    #def get_queryset(self):
    #    stores = Store.objects.filter(owner=self.request.user.id)
    #    return Product.objects.filter(store__in=stores)

class StoreViewset(ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [ permissions.AllowAny ] #RESTRICT TO ADMIN
    queryset = Store.objects.all()

    #def get_queryset(self):
    #   return Store.objects.filter(owner=self.request.user)

class ContactViewset(ModelViewSet):
    model = ContactSerializer
    permission_classes = [ permissions.IsAdminUser, IsOwner ]