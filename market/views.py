from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MarketSerializer, KassaSerializer, SupplierSerializer
from .models import Market, Kassa, Supplier


class MarketList(generics.ListCreateAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def perform_create(self, serializer):
        serializer.save(market=self.request.user)


class MarketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class KassaList(generics.ListCreateAPIView):
    queryset = Kassa.objects.all()
    serializer_class = KassaSerializer


class KassaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kassa.objects.all()
    serializer_class = KassaSerializer


class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer