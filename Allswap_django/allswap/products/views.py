from django.shortcuts import render
from django.views import generic
from django.forms import ModelForm
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                    PermissionRequiredMixin)
from . import models
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.utils.text import slugify
from django.contrib import messages
from django.http import Http404

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class ProductsList(generic.ListView):
    context_object_name = "product_list"
    model = models.Product
    template_name = "products/products_list.html"
    paginate_by = 5

class UserProducts(LoginRequiredMixin, generic.ListView):
    model = models.Product
    template_name = "products/product_user_list.html"
    
    def get_queryset(self):
        try:
            self.product_user = User.objects.prefetch_related('user_products').get(username__iexact = self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        return self.product_user.user_products.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['product_user'] = self.product_user
        return context


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
        self.object.username = self.request.user
        self.object.save()
        return super().form_valid(form)
