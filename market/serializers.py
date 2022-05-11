from rest_framework import serializers

from product.models import Product
from .models import Market, Kassa, Supplier



class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'name']


class KassaProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']


class KassaSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only=True)
    total_price = serializers.CharField(source='get_total_price_of_products')
    products = serializers.SerializerMethodField('get_products')

    def get_products(self, obj):
        return obj.market.product_set.all().values_list(
            'id', 'name', 'price', 'quantity')

    class Meta:
        model = Kassa
        fields = [
            'id', 'name', 'market', 'products', 'total_price',
        ]
        

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'company_name', ]
