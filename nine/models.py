from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    No = models.CharField(max_length=3)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now=False)
    nickname = models.CharField(max_length=100, blank=True)


admin.site.register(Person)
