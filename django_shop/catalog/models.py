from django.db import models
from django.urls import reverse


class Category(models.Model):

    CHOICES = (
        ('Одежда и обувь', 'Одежда и обувь'),
        ('Бытовая техника', 'Бытовая техника'),
        ('Строительный инвентарь', 'Строительный инвентарь'),
        ('Медицинские товары', 'Медицинские товары'),
    )

    title = models.CharField(choices=CHOICES, max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs=[self.slug])

    def get_product_list(self):
        products = [product for product in self.products.all()]
        return products


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=20)
    price = models.FloatField()
    product_pic = models.ImageField()
    description = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'category_slug': self.category.slug,
                                                  'pk': self.pk})

    def add_to_cart(self):
        return reverse('cart:add_to_cart', args=[self.pk])

    def remove_from_cart(self):
        return reverse('cart:remove_from_cart', args=[self.pk])