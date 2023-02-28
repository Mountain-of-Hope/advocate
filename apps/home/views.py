# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import PaymentForm, ChurchForm, DonorForm, StudentForm
from django.urls import reverse
from .models import Payment, Student, Church, Donor
from django.shortcuts import render
from datetime import datetime


@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            pay = Payment()
            pay.donor = form['donor'].data
            pay.amount = form['amount'].data
            pay.checkNumber = form['checkNumber'].data
            pay.date = form['date'].data
            pay.purpose = form['purpose'].data
            pay.method = form['method'].data

            pay.save()
            return HttpResponseRedirect('payments.html')
    else:
        form = PaymentForm()
        context = {'form':form}
        # context['form'] = form
    
    #context = {'segment': 'index'}
    context['segment'] = 'index'

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def pages(request):
    pays = Payment.objects.all()
    students = Student.objects.all()
    context = {'payments':pays}
    context = {'students':students}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        # hacked, needs to be refactored, extract to individual methods
        if load_template == 'payments.html':
            if request.method == 'POST':
                form = PaymentForm(request.POST)
                if form.is_valid():
                    pay = Payment()
                    pay.donor = form['donor'].data
                    pay.amount = form['amount'].data
                    pay.checkNumber = form['checkNumber'].data
                    pay.date = form['date'].data
                    pay.purpose = form['purpose'].data
                    pay.method = form['method'].data
                    pay.save()
                    
                    return HttpResponseRedirect('payments.html')
            else:
                form = PaymentForm()
                context['form'] = form
            
        if load_template == 'students.html':
            form = StudentForm(request.POST)
            if form.is_valid():
                student = Student()
                student.name = form['name'].data
                student.dob = form['dob'].data
                student.community = form['community'].data
                student.program = form['program'].data
                student.grade = form['grade'].data
                student.enroll_date = datetime.now()
                student.save()
        
                return HttpResponseRedirect('students.html')
            else:
                form = StudentForm()
                context['form'] = form
                    
        
        
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    #except:
        #html_template = loader.get_template('home/page-500.html')
        #return HttpResponse(html_template.render(context, request))
