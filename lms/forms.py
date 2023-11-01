from django import forms


from .models import *

class BeTeacherForm(forms.ModelForm):
    class Meta:
        model = BeTeacher
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class Register_project_form(forms.ModelForm):
    class Meta:
        model = Register_project
        fields = [
            'your_name',
            'your_designation',
            'your_email',
            'your_phone',
            'your_image',
            'project_url',
            'project_title',
            'project_language',
            'project_screen_short',
            'project_price',
            'project_position']