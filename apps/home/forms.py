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
        fields = "__all__"

class StudentForm(ModelForm):
    class Meta:
        model = Beneficiary
        fields = "__all__"

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = "__all__"


class SponsorshipTypeForm(ModelForm):
    class Meta:
        model = SponsorshipType
        fields = "__all__"