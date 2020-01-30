from django.db import models

# Create your models here.

from django.forms import ModelForm 
from products import models.Product


class ProductForm(ModelForm):
    class Meta: 
        model = Product
        fields = ['name','courseID','categoryID','price','description','image']

