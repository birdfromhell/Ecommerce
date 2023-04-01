from email.mime import image

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=10)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='category',null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=10)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/product")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title
