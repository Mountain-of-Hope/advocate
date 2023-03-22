# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.core.paginator import Paginator
from .forms import PaymentForm, ChurchForm, DonorForm, StudentForm, ProgramForm
from django.urls import reverse
from .models import Payment, Student, Church, Donor, Program, AddressField
from django.shortcuts import render, redirect
from datetime import datetime
import csv, io

@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            pay = Payment()
            pay.donor = Donor.objects.get(pk=form['donor'].data)
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

def Sponsor_Add(request):

        if request.method == 'POST':
            form = DonorForm(request.POST)
            if form.is_valid():
                donor = form.save(commit=False)
                donor.save()
            else:
                form = DonorForm()
            return HttpResponseRedirect('../sponsors.html')
        

                


# needs to be refactored to use dedicated functions for each view
@login_required(login_url="/login/")
def pages(request):
    pays = Payment.objects.all()
    students = Student.objects.all()
    donors = Donor.objects.all()


    projects = Program.objects.all()
    churches = Church.objects.all()
    context = {'students':students,
               'payments':pays,
               'donors':donors,
               'projects':projects,
               'churches':churches
               }
    

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        if load_template == 'overfunded.html':
            # Formula for overfunded:
            # pull all student objects 
            # add up how much they should have in the 'account'
            # if greater than 'account' value, add to list 
            # return all overfunded students
            students = Student.objects.all()



        
        # hacked, needs to be refactored, extract to individual methods
        if load_template == 'payments.html':
            if request.method == 'POST':
                form = PaymentForm(request.POST)
                if form.is_valid():
                    pay = Payment()
                    pay.donor = Donor.objects.get(pk=form['donor'].data)
                    pay.amount = form['amount'].data
                    pay.checkNumber = form['checkNumber'].data
                    pay.date = form['date'].data
                    pay.student = Student.objects.get(pk=form['student'].data)
                    pay.method = form['method'].data
                    pay.save()
                    
                    return HttpResponseRedirect('payments.html')
            else:
                form = PaymentForm()
                context['form'] = form
                
            
        if load_template == 'students.html':
            form = StudentForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.enroll_date = datetime.now()
                student.save()
                newSponsor = form.cleaned_data['sponsor'].first()
                student.sponsor.add(newSponsor)
                form.save_m2m()
                
                

                return HttpResponseRedirect('students.html')
            else:
                form = StudentForm()
                context['form'] = form


        
        if load_template == 'sponsors.html':
            form = DonorForm(request.POST)
            if form.is_valid():
                donor = form.save(commit=False)
                donor.save()
        
                return HttpResponseRedirect('sponsors.html')
            else:
                form = DonorForm()
                context['form'] = form

        if load_template == 'programs.html':
            form = ProgramForm(request.POST)
            if form.is_valid():
                program = Program()
                program.name = form['name'].data
                program.type = form['type'].data
                program.description = form['description'].data
                program.save()

                return HttpResponseRedirect('programs.html')
            else:
                form = ProgramForm()
                context['form'] = form

        if load_template == 'groups.html':
            form = ChurchForm(request.POST)
            if form.is_valid():
                church = form.save(commit=False)
                church.save()

                return HttpResponseRedirect('groups.html')
            else:
                form = ChurchForm()
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

@login_required(login_url="/login/")
def Payment_Detail(request, id):
    payment = Payment.objects.get(id=id)
    template = loader.get_template('home/payment.html')

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../payments.html')
    else:
        payform = PaymentForm(instance=payment)

    context = {
        'payment':payment,
        'form':payform,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def Group_Detail(request, id):
    group = Church.objects.get(id=id)
    template = loader.get_template('home/group.html')

    if request.method == 'POST':
        form = ChurchForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../groups.html')
    else:
        initial_data = {
            'name':group.name,
            'address':group.address.raw,
            'email':group.email,
            'phone':group.phone
        }
        form = ChurchForm(instance=group, initial=initial_data)

    context = {
        'group':group,
        'form':form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def Sponsor_Detail(request, id):
    sponsor = Donor.objects.get(id=id)
    template = loader.get_template('home/sponsor.html')


    # TODO: fix address updating... currently, it just creates an entirely new record in address table
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=sponsor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../sponsors.html')
    else:
        initial_data = {
            'name':sponsor.name,
            'address':sponsor.address.raw,
            'email':sponsor.email,
            'phone':sponsor.phone,
            'church':sponsor.church
        }
        sponsorform = DonorForm(instance=sponsor, initial=initial_data) 

    context = {
        'sponsor':sponsor,
        'form': sponsorform,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def Student_Detail(request, id):
    student = Student.objects.get(id=id)
    template = loader.get_template('home/student.html')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../students.html')
    else:
        form = StudentForm(instance=student) 

    context = {
        'student':student,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def Program_Detail(request, id):
    program = Program.objects.get(id=id)
    template = loader.get_template('home/program.html')

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../programs.html')
    else:
        form = ProgramForm(instance=program) 

    context = {
        'program':program,
        'form':form,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
def Delete_Data(request):
    
    Payment.objects.all().delete()
    Program.objects.all().delete()
    Donor.objects.all().delete()
    Student.objects.all().delete()
    Church.objects.all().delete()

    
    return HttpResponseRedirect('../')

#test upload
@login_required(login_url="/login/")
def Upload(request):
    if request.method=='POST':
        upload = request.FILES['doc']
        file = upload.read().decode('utf-8')

        reader = csv.DictReader(io.StringIO(file))

        data = [line for line in reader]

        for d in data:
            print(d)

        print(data)

        return HttpResponseRedirect('../')
    
@login_required(login_url="/login/")
def Upload_Sponsors(request):
    if request.method=='POST':
        upload = request.FILES['doc']
        file = upload.read().decode('utf-8')

        reader = csv.DictReader(io.StringIO(file))

        data = [line for line in reader]

        for d in data:
            created = Donor(
                name = d['sponsor_Name'],
                email = d['sponsor_email'],
                phone = d['phone'],
                address = d['address']
                )
            created.save() 

        return HttpResponseRedirect('../sponsors.html')

@login_required(login_url="/login/")
def Upload_Students(request):
    if request.method=='POST':
        upload = request.FILES['doc']
        file = upload.read().decode('utf-8')

        reader = csv.DictReader(io.StringIO(file))

        data = [line for line in reader]

        for d in data:
            created = Student(
                name = d['name'],
                program = Program.objects.get(name=d['program']),
                community = d['community'],
                grade = d['grade'],
                enroll_date = datetime.now()
                )
            created.save()   

        print(data)

        return HttpResponseRedirect('../students.html')

def display_latestnews(request):
    
    newsdata = Donor.objects.all()
    # articles per page
    per_page = 4
    # Paginator in a view function to paginate a queryset
    # show 4 news per page
    obj_paginator = Paginator(newsdata, per_page)
    # list of objects on first page
    first_page = obj_paginator.page(1).object_list
    # range iterator of page numbers
    page_range = obj_paginator.page_range

    context = {
    'obj_paginator':obj_paginator,
    'first_page':first_page,
    'page_range':page_range
    }
    #
    if request.method == 'POST':
        #getting page number
        page_no = request.POST.get('page_no', None) 
        results = list(obj_paginator.page(page_no).object_list.values('id', 'title','content'))
        return JsonResponse({"results":results})

    return render(request, 'home/test.html',context)