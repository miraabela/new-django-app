from django.db import models

# Create your models here.

class Person(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    bio=models.TextField(blank=True, null=True)
    birthDate=models.DateTimeField(blank=True, null=True)
    birthPlace=models.CharField(max_length=100, blank=True, null=True)