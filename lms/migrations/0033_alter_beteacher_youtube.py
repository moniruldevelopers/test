# Generated by Django 4.2.6 on 2023-11-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0032_remove_student_feedback_section_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beteacher',
            name='youtube',
            field=models.URLField(error_messages='Enter Valid URL', max_length=100),
        ),
    ]