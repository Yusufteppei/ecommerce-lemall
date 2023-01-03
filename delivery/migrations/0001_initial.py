# Generated by Django 4.1.2 on 2022-11-26 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("address", "0003_auto_20200830_1851"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryCompany",
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
                ("name", models.CharField(max_length=64)),
                ("deliverable_regions", models.ManyToManyField(to="address.locality")),
                ("states", models.ManyToManyField(to="address.state")),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryRider",
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
                ("full_name", models.CharField(max_length=64)),
                (
                    "delivery_company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="delivery.deliverycompany",
                    ),
                ),
                ("regions", models.ManyToManyField(to="address.locality")),
            ],
        ),
    ]
