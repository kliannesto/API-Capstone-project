from django.db import models

# Create your models here.

class Course(models.Model):
    name= models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
