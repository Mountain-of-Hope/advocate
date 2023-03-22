# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    # Student Details
    path('payment/<int:id>', views.Payment_Detail, name='payment_details'),
    path('sponsor/<int:id>', views.Sponsor_Detail, name='sponsor_details'),
    path('sponsors/add', views.Sponsor_Add, name='sponsor_details'),
    path('student/<int:id>', views.Student_Detail, name='student_details'),
    path('program/<int:id>', views.Program_Detail, name='program_details'),
    path('group/<int:id>', views.Group_Detail, name='group_details'),
    path('setup/upload', views.Upload, name='upload'),
    path('sponsors/upload', views.Upload_Sponsors, name='upload_sponsors'),
    path('students/upload', views.Upload_Students, name='upload_students'),
    path('latestnews', views.display_latestnews, name="display_pagination"),


    # REMOVE IN PRODUCTION, FOR TESTING ONLY
    path('sdfkj2944ss/delete.html', views.Delete_Data, name='delete_data'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
