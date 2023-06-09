# Generated by Django 4.1.2 on 2022-12-16 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
        ("delivery", "0002_deliverycompany_locations_package"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReceivedOrder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_out_date", models.DateTimeField(auto_now_add=True)),
                ("processed", models.BooleanField(default=False)),
                ("on_transit", models.BooleanField(default=False)),
                ("delivered", models.BooleanField(default=False)),
                (
                    "delivery_address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="address.address",
                    ),
                ),
                (
                    "delivery_rider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="delivery.deliveryrider",
                    ),
                ),
            ],
        ),
    ]
