# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.forms import ModelForm
from .models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
