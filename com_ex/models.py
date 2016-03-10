# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)


class Document(models.Model):
    education = models.CharField(max_length=250)
    person = models.ForeignKey(Person)
