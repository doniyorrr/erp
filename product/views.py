from unicodedata import category
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from market.models import Market
from .models import Product, Category, MoveProduct, ReturnedProduct, SubCategory, TrashProduct
from product.permissions import (
    IsProductOwner, IsMoveProductOwner, IsReturnedProductOwner, IsCategoryOwner, IsSubCategoryOwner,
    IsTrashProductOwner)
from .serializers import (
        ProductSerializer, CategorySerializer, MoveProductSerializer, ProductSerializer,
        ReturnedProductSerializer, SubCategorySerializer, TrashProductSerializer 
    )



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Category.objects.filter(sub_category__user=self.request.user.pk)
        print(qs)
        return qs


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsCategoryOwner]


class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = SubCategory.objects.filter(user=self.request.user.pk)
        return qs


class SubCategoryCreateView(generics.CreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsSubCategoryOwner]


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Product.objects.filter(market__user=self.request.user.pk)
        return qs


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(market=self.request.user.market)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsProductOwner]


class MoveProductListCreateView(generics.ListCreateAPIView):
    queryset = MoveProduct.objects.all()
    serializer_class = MoveProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = MoveProduct.objects.filter(product__market__user=self.request.user.pk)
        return qs
    

    def perform_create(self, serializer):
        serializer.save(from_market=self.request.user.market)



class MoveProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = MoveProduct.objects.all()
    serializer_class = MoveProductSerializer
    permission_classes = [IsMoveProductOwner]


class ReturnedProductListCreateView(generics.ListCreateAPIView):
    queryset = ReturnedProduct.objects.all()
    serializer_class = ReturnedProductSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        qs = super().get_queryset()
        qs = ReturnedProduct.objects.filter(product__market__user=self.request.user.pk)
        return qs


    def perform_create(self, serializer):
        serializer.save(from_market=self.request.user.market)


class ReturnedProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = ReturnedProduct.objects.all()
    serializer_class = ReturnedProductSerializer
    permission_classes = [IsReturnedProductOwner]


class TrashProductListCreateView(generics.ListCreateAPIView):
    queryset = TrashProduct.objects.all()
    serializer_class = TrashProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        qs = TrashProduct.objects.filter(product__market__user=self.request.user.pk)
        return qs


    def perform_create(self, serializer):
        serializer.save(market=self.request.user.market)


class TrashProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = TrashProduct.objects.all()
    serializer_class = TrashProductSerializer
    permission_classes = [IsTrashProductOwner]




























