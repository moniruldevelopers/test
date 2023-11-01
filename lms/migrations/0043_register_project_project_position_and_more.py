# Generated by Django 4.2.6 on 2023-11-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0042_alter_register_project_project_screen_short_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_project',
            name='project_position',
            field=models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register_project',
            name='project_url',
            field=models.URLField(unique=True),
        ),
    ]