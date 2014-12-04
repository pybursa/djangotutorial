from django.db import models
import datetime
from datetime import date
import csv

# Create your models here.
from django.db import models

class Person:

    surname = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50)
    birth_date = models.DateTimeField(default=datetime.datetime.now())
    state_province = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)

    # Person initializer
    def __init__(self, surname, first_name, birth_date, nickname=None):
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(int(birth_date[0:4]), int(birth_date[5:7]), int(birth_date[8:10]))

        if nickname is not None:
            self.nickname = nickname

    # Return age of person in str.
    def get_age(self):
        r = date.today() - self.birth_date
        print dir(r)
        return str(int(r.days / 365.25))

    # return fullname of person.
    def get_fullname(self):
        return self.surname + ' ' + self.first_name