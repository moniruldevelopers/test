# Generated by Django 4.2.6 on 2023-10-27 17:39

from django.db import migrations, models
import lms.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_rename_company_fb_team_member_person_fb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=lms.models.UploadToPath('Team_members')),
        ),
    ]