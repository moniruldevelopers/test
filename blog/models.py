from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
# Create your models here.
from django.dispatch import receiver
from django.utils.deconstruct import deconstructible
from django.db.models.signals import pre_delete, pre_save
#for delete 
@deconstructible
class UploadToPath:
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        old_instance = instance.__class__.objects.filter(pk=instance.pk).first()
        if old_instance:
            old_instance.image.delete(save=False)
        return f"{self.path}/{filename}"



class Category_blog(models.Model):
    title = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.title


class Author_blog(models.Model):
    name = models.CharField(max_length=50, null=False)
    designation = models.CharField(max_length=50,null=False)
    image = models.ImageField(upload_to= UploadToPath('blog_img/blog_author/'),null=False)
    def __str__(self):
        return self.name

@receiver(pre_delete, sender=Author_blog)
def delete_media_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


class Blog(models.Model):
    title = models.CharField(max_length=250, null=False)
    description = RichTextField(null=False)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300, unique=True, blank=True)
    tags = TaggableManager()    
    category_blog = models.ForeignKey(Category_blog, on_delete=models.CASCADE)
    author = models.ForeignKey(Author_blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= UploadToPath('blog_img/'),null=False)
    def __str__(self):
        return self.title

@receiver(pre_save, sender=Blog)
def generate_slug(sender, instance, *args, **kwargs):
        if not instance.slug or instance.slug != slugify(instance.title):
          instance.slug = slugify(instance.title)

@receiver(pre_delete, sender=Blog)
def delete_media_files(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
