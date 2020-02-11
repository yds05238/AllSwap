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
from django.db.models import Q

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class ProductsList(generic.ListView):
    context_object_name = "product_list"
    model = models.Product
    template_name = "products/products_list.html"
    paginate_by = 8

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
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteProduct(LoginRequiredMixin, generic.DeleteView):
    model = models.Product
    template_name = "products/product_confirm_delete.html"
    success_url = reverse_lazy('products:list')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)

class SearchProduct(generic.ListView):
    model = models.Product
    context_object_name = "search_result"
    template_name = "products/product_search.html"
    def get_queryset(self):
        query = self.request.GET.get('search_name')
        object_list = models.Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
        