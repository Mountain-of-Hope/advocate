# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.
# Program choices
PAYMENT_INTERVALS = (
    (1, "Monthly"),
    (3, "Quarterly"),
    (6, "Biannual"),
    (12, "Yearly"),
)

class Person(models.Model):
    name = models.CharField(max_length=70)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class SponsorshipType(models.Model):
    name = models.CharField(max_length=35)
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(blank=True)
    members = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)

class Donation(models.Model):
    pass

class Beneficiary(Person):
    pass
    
class Sponsorship(models.Model):
    type = models.ForeignKey(SponsorshipType, on_delete=models.CASCADE)
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    interval = models.CharField(max_length=20, choices=PAYMENT_INTERVALS, default='Monthly')

class Donor(Person):
    sponsorship = models.ManyToManyField(Sponsorship, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    donations = models.ManyToManyField(Donation,blank=True, null=True)

