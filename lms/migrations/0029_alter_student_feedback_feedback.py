# Generated by Django 4.2.6 on 2023-11-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0028_alter_student_feedback_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_feedback',
            name='feedback',
            field=models.TextField(error_messages='give feedback about between 300 char'),
        ),
    ]