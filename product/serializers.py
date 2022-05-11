from rest_framework import serializers
from django.db.models import F, Sum

from market.models import Market, Supplier
from .models import Product, Category, ReturnedProduct, SubCategory, MoveProduct, TrashProduct
from market.serializers import MarketSerializer, SupplierSerializer



class CategorySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Category
        fields = ["id", "title"]


class SubCategorySerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(sub_category__user=self.context['request'].user.pk)

        
    class Meta:
        model = SubCategory
        fields = ['id', 'title', 'category']

class ProductSerializer(serializers.ModelSerializer):
    market = MarketSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'market', 'supplier', 'category', 'sub_category', 'name', 'bar_code', 'plu_code','quantity', 
        'unit', 'price', 'discount', 'discount_price', 'expiry_date', 'received_date', 'date_of_manufacture'
        ]
        read_only_fields = ['market', 'plu_code', 'discount_price']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sub_category'].queryset = SubCategory.objects.filter(user=self.context['request'].user.pk)
        self.fields['category'].queryset = Category.objects.filter(sub_category__user=self.context['request'].user.pk)
        self.fields['supplier'].queryset = Supplier.objects.filter(user=self.context['request'].user.pk)


class MoveProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField('total_price_for_all', read_only=True)
    total_price_for_single = serializers.IntegerField(source='get_single_product_price', read_only=True)
    total_quantity = serializers.SerializerMethodField('total_quantity_for_all', read_only=True)


    def total_price_for_all(self, obj):
        p = MoveProduct.objects.all().annotate(get_total=F('product__price') * F('quantity')).aggregate(total=Sum('get_total'))
        return p


    def total_quantity_for_all(self, obj):
        p = MoveProduct.objects.all().annotate(get_total=F('quantity')).aggregate(all=Sum('get_total'))
        return p

    def __init__(self, *args, **kwargs):
        super(MoveProductSerializer, self).__init__(*args, **kwargs)
    
        self.fields['product'].queryset = Product.objects.filter(market__user=self.context['request'].user.pk)
        self.fields['to_market'].queryset = Market.objects.exclude(user=self.context['request'].user.pk)
        

    class Meta:
        model = MoveProduct
        fields = ['id', 'from_market', 'to_market', 'product', 'quantity','total_price_for_single',
            'total_quantity', 'total_price', 'sent_date']
        read_only_fields = ['from_market']


class ReturnedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnedProduct
        fields = ['id', 'product', 'from_market', 'supplier',  'quantity', 'sent_date', 'is_returned' ]
        read_only_fields = ['from_market']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].queryset = Product.objects.filter(market__user=self.context['request'].user.pk)
        self.fields['supplier'].queryset = Supplier.objects.filter(user=self.context['request'].user.pk)


class TrashProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashProduct
        fields = ['id', 'product', 'market', 'quantity', 'thrown_date']
        read_only_fields = ['id','market']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['product'].queryset = Product.objects.filter(market__user=self.context['request'].user.pk)








































































