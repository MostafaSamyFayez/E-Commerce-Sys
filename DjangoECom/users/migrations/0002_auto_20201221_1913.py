# Generated by Django 3.1.4 on 2020-12-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(default='media/profile_pic.png', upload_to=''),
        ),
    ]