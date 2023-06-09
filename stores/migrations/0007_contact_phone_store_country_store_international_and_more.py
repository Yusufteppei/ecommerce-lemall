# Generated by Django 4.1.2 on 2023-04-27 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0003_auto_20200830_1851'),
        ('stores', '0006_alter_product_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.country'),
        ),
        migrations.AddField(
            model_name='store',
            name='international',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(default=0, verbose_name='Price(In Naira)'),
        ),
    ]
