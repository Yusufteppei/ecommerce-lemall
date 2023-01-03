from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Store, Product
from .views import StoreViewset, ProductViewset, CategoryViewset

router = DefaultRouter()

router.register('stores', StoreViewset, basename='store')
router.register('products', ProductViewset, basename='product')
router.register('categories', CategoryViewset, basename='category')

urlpatterns = [
    path('api/', include(router.urls))
]
