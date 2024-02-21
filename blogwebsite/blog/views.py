from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog

#title = models.CharField(max_length=50)
#content = models.TextField(max_length=300)
#summary = models.CharField(max_length=50)
#image1 = models.ImageField(upload_to='blog_images/')
#image2 = models.ImageField(upload_to='blog_images/')
#categories = models.ManyToManyField(Category)


def index(request):
    context = {
        "blogs": Blog.objects.all(),
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    user_blogs = Blog.objects.filter(user=request.user)
    context = {
        "blogs":user_blogs,
    }
    return render(request,"blog/blogs.html",context)

def blog_details(request, id):
    blog = Blog.objects.get(id = id)
    return render(request,"blog/blog-details.html",{"blog":blog})
