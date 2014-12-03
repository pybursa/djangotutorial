from django.db import models
import csv
import datetime
from datetime import date
import math

# Create your models here.

class Square():
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = self.b * self.b - 4 * self.a * self.c
        self.solution = True
        if self.d == 0:
            self.x1, self.x2 = -(self.b/(self.a * 2))
        elif self.d > 0:
            self.x1 = (-self.b + math.sqrt(self.b * self.b - 4 * self.a * self.c))/(self.a * 2)
            self.x2 = (-self.b - math.sqrt(self.b * self.b - 4 * self.a * self.c))/(self.a * 2)
        elif self.d < 0:
            self.solution = False

class Heroes():
    def __init__(self, filename):
        self.persons = []
        fp = open(filename,"rb")
    
        with fp as csvfile:
            n = 0
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                if n > 0:
                    if row[4] != '':
                        user = Person(row[0], row[1], row[2], row[3], row[4])
                    else:
                        user = Person(row[0], row[1], row[2], row[3])
                    self.persons.append(user)
                n += 1


    def get_hero(self, nickname):
        for person in self.persons:
            if person.nickname == nickname:
                return person
        return None

class Person(object):
    def __init__(self, ident, surname, name, bdata, nickname=None):
        self.ident = ident
        self.surname = surname
        self.name = name
        dt = bdata.split("-")
        #print 'bdata', bdata
        #print 'dt', dt
        birth_date = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
        self.birth_date = birth_date
        if nickname is not None:
            self.nickname = nickname
        else:
            self.nickname = ''
