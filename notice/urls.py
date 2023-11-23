from django.urls import path
from .views import *
urlpatterns = [
    path('',  notice_list, name = 'notice_list')
]

