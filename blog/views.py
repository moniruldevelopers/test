from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request, 'blog_list.html', context)

def blog_details(request, slug):
    blogs = Blog.objects.filter(slug=slug) 
    latest_posts = Blog.objects.order_by('-published')[:5]  
    # tags = instance.tags.all()
    context = {
        'blogs':blogs,   
        'latest_posts':latest_posts,  
        # 'instance': instance, 
        # 'tags':tags,  
     
        # 'category':category,
    }
    return render(request, 'blog_details.html',context)