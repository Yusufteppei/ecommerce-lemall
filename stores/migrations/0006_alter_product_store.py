# Generated by Django 4.1.2 on 2022-12-28 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0005_alter_product_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="store",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="stores.store",
            ),
        ),
    ]