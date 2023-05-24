from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Store, Product
from .views import *

router = DefaultRouter()

router.register('stores', StoreViewset, basename='store')
#router.register('products', products, basename='product')
router.register('categories', CategoryViewset, basename='category')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/store/', store, name='store'),
    path('api/products/', products, name='store-products'),
    path('api/product/create/', ProductUpload.as_view(), name='product-upload')
]
