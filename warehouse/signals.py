from django.db.models.signals import post_save
from django.dispatch import receiver
from stores.models import Product as StoreProduct
from warehouse.models import Product as WarehouseProduct


@receiver(post_save, sender=StoreProduct)
def upload_to_warehouse(sender, instance, created, **kwargs):
    print("Stores signal Running")
    #   AFTER SAVING, IF THE STORE PRODUCT IS ACTIVE, IT WILL BE ACCEPTED INTO THE WAREHOUSE
    if instance.active:
        print(f"{instance} is active")
        # IF THE STORE PRODUCT HAS ALREADY BEEN REGISTERED INTO THE WAREHOUSE THEN IT WILL BE FETCHED AND EDITED
        if WarehouseProduct.objects.filter(product=instance).exists():
            print(f"{instance} is in warehouse")
            w_prod = WarehouseProduct.objects.get(product=instance)
            w_prod.active = False   # THE PRODUCT WILL BE ACTIVE OR NOT IN THE WAREHOUSE

        # IF THE STORE PRODUCT IS NEW, A NEW WAREHOUSE PRODUCT POINTING TO THE STORE PRODUCT WIL BE CREATED
        else:
            print(f"{instance} is not in the warehouse")
            w_prod = WarehouseProduct.objects.create(product=instance)
            print(f"Warehouse with {instance} product has been created")
            w_prod.active = True    # THE PRODUCT WILL BE ACTIVE OR NOT IN THE WAREHOUSE
        w_prod.save()
    
    # IF AFTER SAVING, IT IS INACTIVE, IT WILL BE REMOVED FROM THE WAREHOUSE
    else:
        w_prod = WarehouseProduct.objects.get(product=instance)
        w_prod.delete()
        print(f"{instance} has been deleted from warehouse")