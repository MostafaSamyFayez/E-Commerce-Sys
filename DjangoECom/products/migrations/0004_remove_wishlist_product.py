# Generated by Django 3.1.4 on 2020-12-20 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_wishlist_wishlistitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
    ]
