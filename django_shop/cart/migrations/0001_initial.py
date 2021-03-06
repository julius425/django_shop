# Generated by Django 2.2.4 on 2019-09-11 17:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(blank=True, max_length=20)),
                ('order_email', models.EmailField(blank=True, max_length=254)),
                ('order_phone', models.CharField(blank=True, max_length=20)),
                ('order_address', models.CharField(blank=True, max_length=200)),
                ('order_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('ordered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(related_name='items', to='cart.OrderItem')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.Profile')),
            ],
        ),
    ]
