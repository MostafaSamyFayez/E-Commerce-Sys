# Generated by Django 3.1.4 on 2021-01-10 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20210110_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Clothes', 'Clothes'), ('Mobiles', 'Mobiles'), ('TVs', 'TVs'), ('Videogames&Consols', 'Videogames&Consols'), ('PC', 'PC')], max_length=50, null=True),
        ),
    ]
