from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Category, Product
from stores.serializers import ProductSerializer as StoreProductSerializer


class CategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    #product = StoreProductSerializer()
    class Meta:
        model = Product
        fields = '__all__'


class AdminProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
