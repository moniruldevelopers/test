from .models import Company_info
from django.shortcuts import HttpResponse
def get_all_company_info(request):
    cm = Company_info.objects.all()
    context = {
        'cm':cm,
    }
    return context

# views.py


