from django.db import models
from accounts.models import Profile
from catalog.models import Product
from django.urls import reverse
from django.utils import timezone


class OrderItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.title

    def total_item_price(self):
        return self.product.price * self.quantity


# добавить время заказа

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(OrderItem, related_name='items')
    order_name = models.CharField(blank=True, max_length=20)
    order_email = models.EmailField(blank=True)
    order_phone = models.CharField(blank=True, max_length=20)
    order_address = models.CharField(blank=True, max_length=200)
    order_date = models.DateTimeField(blank=True, default=timezone.now)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Order # {}'.format(self.id)

    def get_absolute_url(self):
        return reverse('cart:order', args=[self.profile.pk])

    def total_price(self):
        total = [item.total_item_price() for item in self.items.all()]
        return sum(total)

    def checkout(self):
        self.ordered = True
        return reverse('cart:checkout', args=[self.pk])
