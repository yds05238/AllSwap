from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from braces.views import SelectRelatedMixin
from datetime import timezone
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from . import models

# Create your views here.

class ProductsList(generic.ListView):
    context_object_name = "product_list"
    model = models.Product
    template_name = "products_list.html"


class ProductDetail(generic.DetailView):
    model = models.Product
    template_name = "products_detail.html"
    context_object_name = 'product'
   

class UploadProduct(LoginRequiredMixin,generic.CreateView):
    fields = ('name','price','description')
    model = models.Product