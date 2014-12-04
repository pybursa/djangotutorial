from django.db import models

# Create your models here.


class Nine(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
