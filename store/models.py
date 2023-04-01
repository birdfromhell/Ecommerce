from moneyed import Money, IDR
from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-category', kwargs={'slug': self.slug})


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/product")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def get_price(self):
        price = Money(self.price, IDR)
        return price
