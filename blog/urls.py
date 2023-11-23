from django.urls import path
from .views import *
urlpatterns = [
    path('', blog_list, name = 'blog_list'),
    path('<slug:slug>/', blog_details, name= 'blog_details'),
    # path('<slug:slug>/', blog_details, name= 'blog_details'),
   
]