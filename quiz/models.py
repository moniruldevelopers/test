from django.db import models

# Create your models here.
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 50, unique = True, null=False)
    def __str__(self):
        return self.title


class Quiz_list(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quiz_link = models.URLField( unique=True, max_length=500, null=False)
    quiz_name = models.CharField(max_length= 200,null=False)
    question = models.IntegerField()
    time = models.CharField(max_length=150)

    def __str__(self):
        return self.quiz_name