# Generated by Django 4.2.6 on 2023-10-28 16:00

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_author_blog_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author_blog',
            name='bauthor_img',
            field=models.ImageField(upload_to=blog.models.UploadToPath('blog_img/blog_author/')),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to=blog.models.UploadToPath('blog_img/')),
        ),
    ]