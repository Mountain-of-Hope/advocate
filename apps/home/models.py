# -*- encoding: utf-8 -*-

from django.db import models
from address.models import AddressField
from phonenumber_field.modelfields  import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Program choices
PAYMENT_CHOICES = (
    ("Check", "Check"),
    ("Online", "Online"),
)

class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    address = AddressField(on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone = PhoneNumberField(blank=True)

class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    interval = models.IntegerField(default=1, validators=[MaxValueValidator(12), MinValueValidator(1)])

    def __str__(self):
        return self.name

#TODO: Add primary contact field related to a person class
class Group (Sponsor):
    def __str__(self):
        return self.name
    
class Donor (Sponsor):
    church = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    enroll_date = models.DateField(null=True)
    name = models.CharField(max_length=256)
    dob = models.DateField(null=True)
    community = models.CharField(max_length=255, null=True)
    program = models.ForeignKey(Program,on_delete=models.CASCADE, null=True, blank=True)
    grade = models.CharField(max_length=255, null=True)
    sponsor = models.ManyToManyField(Sponsor, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def GetSponsorName(self):
        return self.sponsor.name
    
class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True) 
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, blank=True)
    method = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='Check')
    checkNumber = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.CharField(default="", max_length=255)