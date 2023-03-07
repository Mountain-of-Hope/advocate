# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import ModelForm
from .models import Payment, Church, Donor, Student, Program


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'

    # we should have a conversation about what info is required
    def __init__(self, *args, **kwargs):
        super(DonorForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = False
        self.fields['email'].required = False
        self.fields['phone'].required = False


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['enroll_date']

class ChurchForm(ModelForm):
    class Meta:
        model = Church
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'