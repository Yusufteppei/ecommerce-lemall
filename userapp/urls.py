from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet, WishlistItemViewSet, WishlistViewSet, OrderViewSet, ProfileViewSet

router = DefaultRouter()
"""
router.register('carts/<int:uid>/', CartViewSet)
router.register('cart-items/<int:uid>/', CartItemViewSet)
router.register('wishlists/<int:wishlist_id>/', WishlistViewSet)
router.register('wishlists/<wishlist_id>/wishlist_items/', WishlistItemViewSet)
router.register('wishlists/<wishlist_id>/wishlist_items/<int:wishlistitem_id>', WishlistItemViewSet)
router.register('profiles/<int:profile_id>/', ProfileViewSet)
router.register('orders/<int:uid>/', OrderViewSet)
router.register('orders/<int:uid>/<int:order_id>', OrderViewSet)
"""

router.register('carts', CartViewSet, basename="cart")
router.register('cartitems', CartItemViewSet, basename="cartitem")
#router.register('cart', CartItemViewSet, basename="cartitem")

router.register('wishlists', WishlistViewSet, basename="wishlist")
router.register('wishlistitems', WishlistItemViewSet, basename="wishlistitem")
router.register('orders', OrderViewSet, basename="order")
router.register('profiles', ProfileViewSet, basename="profile")


urlpatterns = [
    path('api/', include(router.urls))
]
