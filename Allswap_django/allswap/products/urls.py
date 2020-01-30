from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path('',views.ProductsList.as_view(),name = "list"),
    path('uploads/', views.UploadProduct.as_view(), name = "uploads"),
    path('<slug:username>/',views.UserProducts.as_view(),name = "for_user"),
    path('<slug:slug>/',views.ProductDetail.as_view(), name="detail"),
] 
