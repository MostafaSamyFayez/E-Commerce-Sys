# Generated by Django 3.1.4 on 2020-12-20 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201220_0131'),
        ('products', '0002_auto_20201220_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('wishList', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.wishlist')),
            ],
        ),
    ]
