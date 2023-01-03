from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Cart, Wishlist, Profile, Order

User = get_user_model()

#####         PROFILE         #####
"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        print("Profile created")
"""
#####         CART           #####

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):

    if created:
        Cart.objects.create(owner=instance)
        print("Cart Created!")

@receiver(post_save, sender=User)
def update_cart(sender, instance, created, **kwargs):

    if created == False:
        instance.cart.save()
        print("Cart updated!")


#####         WISHLIST           #####

@receiver(post_save, sender=User)
def save_wishlist(sender, instance, created, **kwargs):

    if created:
        Wishlist.objects.create(owner=instance)
        print("Wishlist Created!")
    
    else:
        instance.wishlist.save()
        print("Wishlist updated!")

#@receiver(post_save, sender=User)
#def update_wishlist(sender, instance, created, **kwargs):
#
#   if created == False:
#        instance.wishlist.save()
#       print("Wishlist updated!")


#######         ORDER               #######


@receiver(post_save, sender=Cart)
def create_order(sender, instance, created, **kwargs):

    if instance.is_checked_out:
        order = Order.objects.create(owner=instance.owner)
        print(instance.total)

        for i in list(instance.items.all()):
            order.items.add(i)
        order.save()
        #print("Order Created!")
