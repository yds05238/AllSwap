from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 155, unique = True)

    def __str__(self):
        return self.name

    
class Product(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255)
    courseID = models.SlugField(max_length = 50)
    categoryID = models.ForeignKey(Category, null = True, blank = True, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    slug = models.SlugField()
    description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail',kwargs = {'slug':self.slug})

    class Meta: 
        ordering = ['name']



