from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    summary = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blogs')
    image2 = models.ImageField(upload_to='blogs')
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return self.title

