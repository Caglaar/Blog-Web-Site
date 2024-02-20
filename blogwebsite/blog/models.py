from django.db import models

from account.models import User

class Category(models.Model): 
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    summary = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='blog_images/')
    image2 = models.ImageField(upload_to='blog_images/')
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

