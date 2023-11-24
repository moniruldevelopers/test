from django.urls import path
from .views import *
urlpatterns = [
    path('', courses, name='course_list'),
    path('course_details/', course_details, name='course_details'),
    
]