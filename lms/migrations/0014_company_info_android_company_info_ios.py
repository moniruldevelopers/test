# Generated by Django 4.2.6 on 2023-10-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_company_info_company_logo_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_info',
            name='android',
            field=models.URLField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company_info',
            name='ios',
            field=models.URLField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]