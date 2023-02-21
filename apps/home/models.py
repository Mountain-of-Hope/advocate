# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sponsor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Student(models.Model):
    name = models.CharField(max_length=255)
    
class Payment(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    purpose = models.CharField(max_length=255)
