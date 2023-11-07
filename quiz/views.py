from django.shortcuts import render
from .models import *
# Create your views here.
def quiz(request):
    categories_with_content = Category.objects.filter(quiz_list__isnull=False).distinct()
    post_lists = Quiz_list.objects.filter(category__in=categories_with_content)
    return render(request, 'quiz.html', {'categories_with_content': categories_with_content, 'post_lists': post_lists})
