from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.forms import ModelForm 
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 155, unique = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(User, related_name = "user_products", on_delete = models.CASCADE, null = True)
    name = models.CharField(max_length = 255)
    courseID = models.SlugField(max_length = 50)
    categoryID = models.ForeignKey(Category, null = True, blank = True, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    slug = models.SlugField(editable = False,blank = False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)    
    
    def get_absolute_url(self): 
        return reverse("products:detail", kwargs={"slug": self.slug})

    class Meta: 
        ordering = ['name']


