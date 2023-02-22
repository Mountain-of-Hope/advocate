# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import Payment


class PaymentForm(forms.Form):
    Sponsor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Donor Name",
                "class": "form-control"
            }
        ))
    method = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "How did the donor pay?",
                "class": "form-control"
            }
        ))
    checkNumber = forms.IntegerField(
        widget=forms.IntegerField(
            attrs={
                "placeholder": "Check #",
                "class": "form-control"
            }
        ))
    amount = forms.DecimalField(
        widget=forms.DecimalField(
            attrs={
                "placeholder": "Amount",
                "class": "form-control"
            }
        ))
    date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Date",
                "class": "form-control"
            }
        ))
    purpose = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Purpose",
                "class": "form-control"
            }
        ))




    class Meta:
        model = Payment
        fields = ('donor', 'method', 'checkNumber', 'amount', 'date', 'purpose')
