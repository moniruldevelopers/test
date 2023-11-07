from django.contrib import admin
from .models import *



admin.site.register(Gallery)
admin.site.register(Event)
admin.site.register(Register_project)



admin.site.register(Hero)
admin.site.register(Student_feedback)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Company_info)

#for contact page
admin.site.register(Team_member)
admin.site.register(Newsletter)

#FOR TEACHER REGISTRATIONS
admin.site.register(BeTeacher)