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
    path('donation/<int:id>', views.Donation_Detail, name='donation_details'),
    path('donations.html', views.Donations, name='donations'), 
    path('donation/add', views.Donation_Add, name='donation_add'),
    path('donation/<int:id>/delete', views.Donation_Delete, name='donation_delete'),
    path('sponsor/<int:id>', views.Sponsor_Detail, name='sponsor_details'),
    path('sponsor/<int:id>/delete', views.Sponsor_Delete, name='sponsor_delete'),
    path('sponsorship/<int:id>', views.Sponsorship_Detail, name='sponsorship_details'),
    path('sponsorship/<int:id>/delete', views.Sponsorship_Delete, name='sponsorship_delete'),
    path('sponsors/add', views.Sponsor_Add, name='sponsor_details'),
    path('sponsorship/add', views.Sponsorship_Add, name='sponsorship_add'),
    path('student/<int:id>', views.Student_Detail, name='student_details'),
    path('student/<int:id>/delete', views.Student_Delete, name='student_delete'),
    path('program/<int:id>', views.Program_Detail, name='program_details'),
    path('program/<int:id>/delete', views.Program_Delete, name='program_delete'),
    path('group/<int:id>', views.Group_Detail, name='group_details'),
    path('group/<int:id>/delete', views.Group_Delete, name='group_delete'),
    path('setup/upload', views.Upload, name='upload'),
    path('sponsors/upload', views.Upload_Sponsors, name='upload_sponsors'),
    path('students/upload', views.Upload_Students, name='upload_students'),
    path('sponsor/get_email/<int:id>', views.get_sponsor_email, name='get-sponsor-email'),
    path('sponsor/get_email/', views.get_sponsor_email, name='get-sponsor-email'),
    path('sponsorships.html', views.Sponsorships, name='get-sponsor-email'),


    # REMOVE IN PRODUCTION, FOR TESTING ONLY
    # path('sdfkj2944ss/delete.html', views.Delete_Data, name='delete_data'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
