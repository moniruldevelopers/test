from django.urls import path
from .views import *
urlpatterns = [
    
     path('', home, name = 'home'),  
     path('beteacher/', be_teacher, name='beteacher'),
     path('contact/', contact,name = 'contact'),  
     path('about/', about, name = 'about'),    
     path('project_list/', project, name = 'project'),    
     path('project_form/', project_form, name = 'project_form'),    
     path('gallery/', gallery, name = 'gallery'),    
  
   
]
   

