from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',), 
    }
admin.site.register(Category_blog)
admin.site.register(Author_blog)
admin.site.register(Blog, BlogAdmin)