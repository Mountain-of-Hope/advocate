# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Church, Program, Donor, Student, Payment

# Register your models here.
admin.site.register(Church)
admin.site.register(Program)
admin.site.register(Donor)
admin.site.register(Student)
admin.site.register(Payment)