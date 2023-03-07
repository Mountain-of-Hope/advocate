# -*- encoding: utf-8 -*-

from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields  import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

# Program choices
PROGRAM_CHOICES = (
    ("project", "Project"),
    ("program", "Program"),
)

class Program(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=PROGRAM_CHOICES, default='program')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Church (models.Model):
    name = models.CharField(max_length=255)
    address = AddressField()
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name

class Donor (models.Model):
    name = models.CharField(max_length=255)
    address = AddressField()
    email = models.EmailField(null=True)
    phone = PhoneNumberField(blank=True)
    church = models.ForeignKey(Church, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    enroll_date = models.DateField(null=True)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    community = models.CharField(max_length=255, null=True)
    program = models.ForeignKey(Program,on_delete=models.CASCADE, null=True, blank=True)
    grade = models.CharField(max_length=255, null=True)
    sponsor = models.ManyToManyField(Donor, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(default="check", max_length=255)
    checkNumber = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.CharField(default="", max_length=255)
    purpose = models.CharField(max_length=255)