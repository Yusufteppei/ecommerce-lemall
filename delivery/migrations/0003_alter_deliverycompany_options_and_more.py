# Generated by Django 4.1.2 on 2023-01-04 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_deliverycompany_locations_package'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliverycompany',
            options={'verbose_name_plural': 'Delivery Companies'},
        ),
        migrations.AlterModelOptions(
            name='deliveryrider',
            options={'verbose_name_plural': 'Delivery Riders'},
        ),
    ]