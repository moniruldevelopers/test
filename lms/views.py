from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View, ListView
from .models import *
from django.contrib import messages
from .forms import BeTeacherForm, ContactForm, Register_project_form

# for project register page






def home(request): 
    hero_items = Hero.objects.all() 
    feedback = Student_feedback.objects.order_by('-published')[:3]   
    contex = {
        'hero_items':hero_items,
        'feedback':feedback,
    }
    return render(request, 'home.html',contex)




def project(request):
    project_list = Register_project.objects.filter(accept=True)
    context = {
        'project_list':project_list,
    }
    return render(request, 'components/projects.html',context)

def project_form(request):
    if request.method == 'POST':
        form = Register_project_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message sent successfully')
        else:
            messages.error(request, "Somethings Error to send message")
    else:
        form = Register_project_form()
    return render(request, 'components/project_forms.html',{'form':form})



def be_teacher(request):
    if request.method == 'POST':
        form = BeTeacherForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']  # Extract the email from the form
            if BeTeacher.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                form.save()  # Save the data to the database
                messages.success(request, 'Your information has been submitted successfully.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BeTeacherForm()

    return render(request, 'components/team-become.html', {'form': form})






#for contact page 
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message sent successfully')
        else:
            messages.error(request, "Somethings Error to send message")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
 
#end contact page 

 
#for about page 
def about(request):      
    if request.method == "POST":
        letter = Newsletter()
        email = request.POST.get('email')
        letter.email = email        
        if Newsletter.objects.filter(email = email).exists():
            return HttpResponse("Email already Submitted !")        

        else:
            letter.save()
            return HttpResponse("Email Submitted Success") 

    teams = Team_member.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'about.html',context)

#end about page 