from django.contrib import admin

# Register your models here.
from .models import Product, Category, ShoppingSite


class ReadOnlyFieldsProduct(admin.ModelAdmin):
    pass


admin.site.register(Product, ReadOnlyFieldsProduct)


class ReadOnlyFieldsCategory(admin.ModelAdmin):
    pass


admin.site.register(Category, ReadOnlyFieldsCategory)


class ShoppingSiteFieldsCategory(admin.ModelAdmin):
    pass


admin.site.register(ShoppingSite, ShoppingSiteFieldsCategory)
