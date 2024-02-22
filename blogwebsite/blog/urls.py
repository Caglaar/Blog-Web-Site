from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/index
#http://127.0.0.1:8000/blogs
#http://127.0.0.1:8000/blogs/(değişken int)

urlpatterns = [
    path("",views.index, name="home"),
    path("index",views.index),
    path("blogs",views.blogs, name="blogs"),
    path("blogs/<int:id>",views.blog_details, name="blog_details"),
    path("blogs/write",views.blog_write,name="blogs_write"),
    path("blogs/edit/<int:id>",views.blog_edit,name="blogs_edit"),
    path('blogs/delete/<int:id>', views.blog_delete, name="blogs_delete"),
    path('blogs/catagory/<int:id>', views.blog_by_category, name="blog_by_category")
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)