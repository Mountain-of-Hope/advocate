# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select, Textarea, EmailInput
from .models import Payment, Church, Donor, Student, Program


class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Donor Name'
            }),
            'address': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Donor Address'
            }),
            'email': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Donor Email'
            }),
            'phone': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Donor Phone'
            }),
            'church': Select(attrs={
            'class': 'form-control',
            'placeholder':'Donor Church'
            }),
        }

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
        widgets = {
            'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Student Name'
            }),
            'dob': DateInput(attrs={
            'type':'date',
            'class': 'form-control',
            'placeholder':'Student date of birth'
            }),
            'community': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'In what community does the student live?'
            }),
            'program': Select(attrs={
            'class': 'form-control',
            'placeholder':'To what program does the student belong?'
            }),
            'grade': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'In what grade is the student?'
            }),
        }

    def clean_grade(self, *args, **kwargs):
        grade = self.cleaned_data.get("grade")
        if grade == 'help':
            raise forms.ValidationError("Not a valid K-12 Grade.")
        return grade

class ChurchForm(ModelForm):
    class Meta:
        model = Church
        fields = '__all__'
        widgets ={
           'name': TextInput(attrs={
            'class': 'form-control',
           }),
           'address': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Group address'
           }),
           'email': EmailInput(attrs={
            'class': 'form-control'
           }),
           'phone': TextInput(attrs={
            'type':'tel',
            'class': 'form-control',
            'placeholder':'Format: +1 903 123 0011'
           })
        }

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets ={
           'donor': Select(attrs={
            'class': 'form-control',
            'placeholder':'Donor Name'
           }),
           'method': Select(attrs={
            'class': 'form-control',
            'placeholder':'How did the donor pay?'
           }),
           'checkNumber': NumberInput(attrs={
            'class': 'form-control',
            'placeholder':'If paying by check, what is Check#'
           }),
           'amount': NumberInput(attrs={
            'class': 'form-control',
            'placeholder':'How much?'
           }),
           'date': DateInput(attrs={
            'type':'date',
            'class': 'form-control',
            'placeholder':'Payment Date'
           }),
           'purpose': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'What was this payment for?'
           })
        }

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = '__all__'
        widgets ={
           'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Program/Project name'
           }),
           'type': Select(attrs={
            'class': 'form-control',
            'placeholder':'Program = long-term, Project = short-term'
           }),
           'description': Textarea(attrs={
            'class': 'form-control',
            'placeholder':'Short description of the project/program for other workers to know about'
           })
        }