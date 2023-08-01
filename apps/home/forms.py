# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select, Textarea, EmailInput
from .models import Donation, Group, Donor, Beneficiary, SponsorshipType


class DonorForm(ModelForm):
    class Meta:
        model = Donor

class StudentForm(ModelForm):
    class Meta:
        model = Beneficiary

class GroupForm(ModelForm):
    class Meta:
        model = Group

class DonationForm(ModelForm):
    class Meta:
        model = Donation


class SponsorshipTypeForm(ModelForm):
    class Meta:
        model = SponsorshipType