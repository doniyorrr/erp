from django.contrib import admin

from product.models import Product, Category, MoveProduct, SubCategory, TrashProduct, \
    ReturnedProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_discount", "get_real_price", 'category', 'sub_category', 'quantity')

    def category(self, obj):
        # for i in obj.category.sub_category.title:
        #     name = i.title
        return obj.sub_category.category.title
        
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(MoveProduct)
class MoveProductsAdmin(admin.ModelAdmin):
    list_display = ("from_market", "to_market", "quantity")


@admin.register(ReturnedProduct)
class ReturnedProductAdmin(admin.ModelAdmin):
    list_display = ("from_market", "supplier", "quantity")


@admin.register(TrashProduct)
class TrashProductAdmin(admin.ModelAdmin):
    list_display = ('name', "quantity")

    def name(self, obj):
        return obj.product.name


@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
