# Generated by Django 4.2.6 on 2023-10-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0004_company_info_google_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_info',
            name='google_map',
            field=models.URLField(max_length=500),
        ),
    ]