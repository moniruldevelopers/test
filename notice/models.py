from django.db import models

# Create your models here.
class NoticeBy(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):        
        return self.name

class Notice(models.Model):
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    notice_title = models.CharField(max_length=255)
    notice_by = models.ForeignKey(NoticeBy, on_delete=models.CASCADE)
    notice_for = models.CharField(max_length=25)
    file_upload = models.FileField(upload_to='notice/')
    def __str__(self):
        return self.notice_title

