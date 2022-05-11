from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('create/', views.ProductCreate.as_view(), name='product_create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path("categories/", views.CategoryListView.as_view(), name="category"),
    path("category-create/", views.CategoryCreateView.as_view(), name="category"),
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path("subcategories/", views.SubCategoryListView.as_view(), name="sub_category"),
    path('subcategory-create/', views.SubCategoryCreateView.as_view(), name='subcategory_create'),
    path('subcategory-detail/<int:pk>/', views.SubCategoryDetailView.as_view(), name='subcategory_detail'),

    path("moveproducts/", views.MoveProductListCreateView.as_view(), name="moveproducts"),
    path('moveproduct-detail/<int:pk>/', views.MoveProductDetailView.as_view(), name='moveproduct_detail'),

    path("returnedproducts/", views.ReturnedProductListCreateView.as_view(), name="returnedproducts"),
    path('returnedproduct-detail/<int:pk>/', views.ReturnedProductDetailView.as_view(), name='returnedproduct_detail'),

    path("trashproducts/", views.TrashProductListCreateView.as_view(), name="trashproducts"),
    path('trashproducts-detail/<int:pk>/', views.TrashProductDetailView.as_view(), name='trashproducts_detail'),


]
