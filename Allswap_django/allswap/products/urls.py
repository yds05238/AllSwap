from django.urls import path, include
from . import views
from django.contrib import admin

admin.autodiscover()

app_name = "products"

urlpatterns = [
    path('',views.ProductsList.as_view(),name = "list"),
    path('uploads/', views.UploadProduct.as_view(), name = "uploads"),
    path('product/<slug:slug>/',views.ProductDetail.as_view(), name="detail"),
    path('user/<slug:username>/',views.UserProducts.as_view(),name = "for_user"),
    path('user/delete/<slug:slug>/',views.DeleteProduct.as_view(), name = "delete"),
    path('search/',views.SearchProduct.as_view(), name = 'search'),
] 
