# Generated by Django 4.2.6 on 2023-11-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0039_register_project_project_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_project',
            name='project_title',
            field=models.CharField(max_length=250),
        ),
    ]