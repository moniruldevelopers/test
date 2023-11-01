from django.db import models
from django.core.validators import RegexValidator #for phone
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.deconstruct import deconstructible

# register your project model   
class Register_project(models.Model):
    your_name  = models.CharField(max_length=150, null=False)
    your_designation =models.CharField(max_length=50)
    your_email = models.EmailField(max_length=150, null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
        message="Typical format for a mobile phone number inside Bangladesh is 01XXX NNNNNN, and +880 1XXX NNNNNN when dialed internationally.. Up to 15 digits allowed."
    )

    your_phone = models.CharField(validators=[phone_regex], max_length=17, null= False)
    your_image = models.ImageField(default='', upload_to = 'project_register/', null=True, blank=True)
    project_url = models.URLField(unique=True)
    project_title = models.CharField(max_length=250)
    project_language =models.CharField(max_length=200)
    project_screen_short = models.ImageField(default='', upload_to='project_register/project_ss', null=True, blank=True)
    PROJECT_PRICE = (
        ('Free', 'Free'),
        ('Paid', 'Paid'),
    )
    project_price = models.CharField(max_length=50, choices=PROJECT_PRICE)
    PROJECT_POSITION = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    )
    project_position = models.CharField(max_length=15, choices=PROJECT_POSITION )
    accept = models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.project_title




# for about page 
@deconstructible
class UploadToPath:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        old_instance = instance.__class__.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.image.delete(save=False)
        return f"{self.path}/{filename}"

class Student_feedback(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)
    image = models.ImageField(default='feedback/default.png', upload_to=UploadToPath('feedback/'), error_messages='Upload Your Photo',null=True, blank=True)
    feedback_text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return self.name

@receiver(pre_delete, sender=Student_feedback)
def delete_media_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

class Hero(models.Model):
    image = models.ImageField(upload_to='hero/' , null=True, blank = True,)
    featured_video = models.URLField(null=False)
    workshop_name = models.CharField(max_length=50)
    workshop_join_link = models.URLField(max_length=50)
    hero_slogan = models.CharField(max_length=150, )

# Create your be teacher model  here.
@deconstructible
class UploadToPath:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        old_instance = instance.__class__.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.cv.delete(save=False)
        return f"{self.path}/{filename}"

class BeTeacher(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
        message="Typical format for a mobile phone number inside Bangladesh is 01XXX NNNNNN, and +880 1XXX NNNNNN when dialed internationally.. Up to 15 digits allowed."
    )

    phone = models.CharField(validators=[phone_regex], max_length=17, null= False)
    cv = models.FileField(upload_to='teacher_registraion_files/')
    youtube = models.URLField(max_length=100, null=False, error_messages='Enter Valid URL')
    comment = models.TextField(max_length=500, null=False )
    def __str__(self):
        return self.name
@receiver(pre_delete, sender=BeTeacher)
def delete_media_files(sender, instance, **kwargs):
    if instance.cv:
        instance.cv.delete(save=False)
# end  your be teacher model  here.


class Contact(models.Model):
    name  = models.CharField(max_length=150, null=False)
    email = models.EmailField(max_length=150, null=False)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
        message="Typical format for a mobile phone number inside Bangladesh is 01XXX NNNNNN, and +880 1XXX NNNNNN when dialed internationally.. Up to 15 digits allowed."
    )

    phone = models.CharField(validators=[phone_regex], max_length=17, null= False)
    subject = models.CharField(max_length=300, null=False)
    message = models.TextField(max_length=1000, null=False)
    
    def __str__(self):
        return self.subject

class Company_info(models.Model):
    name = models.CharField(max_length=150)
    quets = models.TextField(max_length=300)
    company_phone = models.CharField(max_length=20)
    company_email = models.EmailField(max_length=50,)
    address = models.CharField(max_length=200)    
    ios = models.URLField(max_length=50)
    android = models.URLField(max_length=50)
    company_fb = models.URLField(max_length=50)
    company_linkdln = models.URLField(max_length=50)
    company_yt = models.URLField(max_length=50)
    company_x = models.URLField(max_length=50)
    google_map = models.CharField(max_length=500)
    company_logo = models.ImageField(upload_to = 'compnay_logo/')
    company_logo_footer = models.ImageField(upload_to = 'compnay_logo/')
   
    def __str__(self):
        return self.name


@deconstructible
class UploadToPath:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        old_instance = instance.__class__.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.image.delete(save=False)
        return f"{self.path}/{filename}"

class Team_member(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)
    person_fb = models.URLField(max_length=50, null=True)
    person_linkdln = models.URLField(max_length=50,null=True)
    person_yt = models.URLField(max_length=50, null=True)    
    image = models.ImageField(upload_to= UploadToPath('Team_members/'))
    def __str__(self):
        return self.name

@receiver(pre_delete, sender=Team_member)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)



class Newsletter(models.Model):
    email = models.EmailField(max_length=50, null=False)
    def __str__(self):
        return self.email


# end about page 


