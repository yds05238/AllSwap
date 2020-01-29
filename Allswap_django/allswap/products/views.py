from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify


from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

# Create your views here.

class ProductsList(generic.ListView):
    context_object_name = "product_list"
    model = models.Product
    template_name = "products/products_list.html"


class ProductDetail(generic.DetailView):
    model = models.Product
    template_name = "products/product_detail.html"
    context_object_name = 'product'

class UploadProduct(LoginRequiredMixin,SelectRelatedMixin, generic.CreateView):
    model = models.Product
    template_name = 'products/product_form.html'
    fields = ['name','courseID','categoryID','price','description','image']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
