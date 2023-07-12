from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"


class Product(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    # price = models.FloatField(max_length=10)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} - {self.title}"

    class Meta:
        verbose_name = "Product"


class ShoppingSite(models.Model):
    site_name = models.CharField(max_length=100, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(max_length=5)

    def __str__(self):
        return f"{self.site_name} - {self.product.category.name} - {self.product.name} - {self.price}"

    class Meta:
        verbose_name = "Shopping Site"