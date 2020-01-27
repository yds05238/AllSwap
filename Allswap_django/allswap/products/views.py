from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from . import models

# Create your views here.

class ProductsList(generic.ListView):
    context_object_name = "product_list"
    model = models.Product
    template_name = "products/products_list.html"


class ProductDetail(generic.DetailView):
    context_object_name = "product_detail"
    model = models.Product
    template_name = "products/product_detail.html"

class UploadProduct(LoginRequiredMixin,generic.CreateView):
    fields = ('name','price','description')
    model = models.Product