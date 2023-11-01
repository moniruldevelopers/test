# Generated by Django 4.2.6 on 2023-10-27 18:05

from django.db import migrations, models
import lms.models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0009_alter_team_member_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='team_member',
            name='img',
            field=models.ImageField(default=0, upload_to=lms.models.UploadToPath('Team_members')),
            preserve_default=False,
        ),
    ]
