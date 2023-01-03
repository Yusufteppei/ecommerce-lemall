from .models import Category, Product, Store, Contact, Image
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CategorySerializer(ModelSerializer):

    def create(self, validated_data):
        print(validated_data.get('title'))
        return super().create(validated_data)
    class Meta:
        model = Category
        fields = '__all__'


class StoreSerializer(ModelSerializer):
    owner = serializers.StringRelatedField()
    class Meta:
        model = Store
        fields = ('name', 'owner', 'id')


class ImageSerializer(ModelSerializer):
    image = serializers.FileField()
    class Meta:
        model = Image
        fields = ('image',)


class ProductSerializer(ModelSerializer):
    #store = StoreSerializer()
    images = ImageSerializer(many=True)
    location = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    
    def create(self, validated_data):
        print("Creating store product model via API")
        images = validated_data.pop("images")
        store_id = validated_data.pop('store')
        #store = Store.objects.get(id=store_id)
        product = Product.objects.create(**validated_data)
        product.images.set(images)
        product.store = store_id
        product.save()
        return product

        
    class Meta:
        model = Product
        #fields = ('title', 'quantity', 'price', 'active', 'category', 'location')
        fields = '__all__'
        #exclude = ('store', )


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
