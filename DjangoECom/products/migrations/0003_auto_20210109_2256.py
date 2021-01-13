# Generated by Django 3.1.4 on 2021-01-09 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20210102_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AddField(
            model_name='product',
            name='total_review',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=250)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False'), ('New', 'New')], default='New', max_length=20)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('rate', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]