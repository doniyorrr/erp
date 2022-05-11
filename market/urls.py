from django.urls import path
from . import views

urlpatterns = [
    path('', views.MarketList.as_view(), name='market_list'),
    path('market-detail/<int:pk>/', views.MarketDetail.as_view(), name='market_detail'),

    path('kassalar/', views.KassaList.as_view(), name='kassa_list'),
    path('kassa-detail/<int:pk>/', views.KassaDetail.as_view(), name='kassa_detail'),


    path('suppliers', views.SupplierList.as_view(), name='supplier_list'),
    path('supplier-detail/<int:pk>/', views.SupplierDetail.as_view(), name='supplier_detail'),
    
]