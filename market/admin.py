from django.contrib import admin

from market.models import Market, Kassa, Supplier


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ("name", 'user')


@admin.register(Kassa)
class KassaAdmin(admin.ModelAdmin):
    list_display = ("market", "name")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("company_name",)