from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()
    
