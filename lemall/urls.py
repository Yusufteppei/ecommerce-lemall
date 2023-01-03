from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("warehouse/", include('warehouse.urls')),
    path("auth/", include('authentication.urls')),
    #path("orders/", include('orders.urls')),
    path("stores/", include('stores.urls')),
    #path("HR/", include('HR.urls')),
    #path("delivery/", include('delivery.urls')),
    path("userapp/", include('userapp.urls'))
]
