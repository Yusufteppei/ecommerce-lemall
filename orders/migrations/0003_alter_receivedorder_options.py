# Generated by Django 4.1.2 on 2023-01-04 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receivedorder',
            options={'verbose_name_plural': 'Received Orders'},
        ),
    ]
