from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
from address.models import Locality, Address


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")
    
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        customer_group = Group.objects.get(name='Customer')

        user.set_password(password)
        user.save()
        user.groups.add(customer_group)
        return user

    def create_vendor_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")
    
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        vendor_group = Group.objects.get(name='Vendor')

        user.set_password(password)
        user.save()
        user.groups.add(vendor_group)
        return user

    def create_superuser(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")
    
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email


class UserContact(models.Model):
    user_account = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    region = models.ForeignKey(Locality, on_delete=models.PROTECT, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=16, default='000')
    
    def __str__(self):
        return f'{self.user_account} contact'
