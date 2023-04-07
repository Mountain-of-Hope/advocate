# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Group, Program, Donor, Student, Payment, Sponsor

# Register your models here.
admin.site.register(Group)
admin.site.register(Sponsor)
admin.site.register(Program)
admin.site.register(Donor)
admin.site.register(Student)
admin.site.register(Payment)