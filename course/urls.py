from django.urls import path
from .views import *
urlpatterns = [
    path('', courses, name='course_list')
    
]