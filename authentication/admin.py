from django.contrib import admin
from .models import UserAccount, UserContact
# Register your models here.

admin.site.register(UserAccount)
admin.site.register(UserContact)
