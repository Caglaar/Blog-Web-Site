from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from blog.models import Blog,Category

#title = models.CharField(max_length=50)
#content = models.TextField(max_length=300)
#summary = models.CharField(max_length=50)
#image1 = models.ImageField(upload_to='blog_images/')
#image2 = models.ImageField(upload_to='blog_images/')
#categories = models.ManyToManyField(Category)


def index(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all(),
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    user_blogs = Blog.objects.filter(user=request.user)
    context = {
        "blogs":user_blogs,
        "categories": Category.objects.all(),
    }
    return render(request,"blog/blogs.html",context)


def blog_details(request, id):
    blog = Blog.objects.get(id = id)
    return render(request,"blog/blog-details.html",{"blog":blog})

def blog_write(request):
    context = {
        "categories": Category.objects.all(),
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        summary = request.POST.get('summary')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        category_ids = request.POST.getlist('categories')  # Checkbox'ların değerlerini al

        if not category_ids:
            return HttpResponseBadRequest("At least one category must be selected.")

        categories = Category.objects.filter(id__in=category_ids)

        # Blog modeli oluştur ve kaydet
        blog = Blog.objects.create(
            title=title,
            content=content,
            summary=summary,
            image1=image1,
            image2=image2,
            user=request.user
        )
        blog.categories.set(categories)
        return redirect("blogs")

    return render(request,"blog/blog-write.html",context)

def blog_edit(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        summary = request.POST.get('summary')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        category_ids = request.POST.getlist('categories')

        # Kategori nesnelerini al
        categories = Category.objects.filter(id__in=category_ids)

        # Blog nesnesini güncelle
        blog.title = title
        blog.content = content
        blog.summary = summary
        if image1:
            blog.image1 = image1
        if image2:
            blog.image2 = image2

        # Kategorileri güncelle
        blog.categories.set(categories)
        
        # Değişiklikleri kaydet
        blog.save()

        # Kullanıcıyı blog detayları sayfasına yönlendir
        return HttpResponseRedirect(reverse('blog_details', args=[blog.id]))

    # GET isteği geldiğinde, blog düzenleme formunu göster
    context = {
        'blog': blog,
        'categories': Category.objects.all(),
    }
    return render(request, "blog/blog-edit.html", context)


def blog_delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("home") 

def blog_by_category(request, id):
    category = Category.objects.get(id=id)
    blogs_in_category = Blog.objects.filter(categories=id)
    
    context = {
        "blogs": blogs_in_category,
        "category": category,
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)