from django.shortcuts import render
from .models import Notice

def notice_list(request):
    notices = Notice.objects.all().order_by('-created_date', '-created_time')[:2]
    context ={
        'notices': notices,
    }
    return render(request, 'notice_list.html', context)


