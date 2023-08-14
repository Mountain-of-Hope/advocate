# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Group, SponsorshipType, Donor, Beneficiary, Donation

# Register your models here.
admin.site.register(Group)
admin.site.register(SponsorshipType)
admin.site.register(Donor)
admin.site.register(Beneficiary)
admin.site.register(Donation)