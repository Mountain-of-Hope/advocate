# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import PaymentForm
from django.urls import reverse
from .models import Payment
from django.shortcuts import render


@login_required(login_url="/login/")
def index(request):

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            test = Payment()
            test.donor = form['donor'].data
            test.amount = form['amount'].data
            test.checkNumber = form['checkNumber'].data
            test.date = form['date'].data
            test.purpose = form['purpose'].data
            test.method = form['method'].data

            test.save()
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
    context = {'payments':pays}

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        
        # hacked, needs to be refactored
        if load_template == 'payments.html':
            if request.method == 'POST':
                form = PaymentForm(request.POST)
                if form.is_valid():
                    test = Payment()
                    test.donor = form['donor'].data
                    test.amount = form['amount'].data
                    test.checkNumber = form['checkNumber'].data
                    test.date = form['date'].data
                    test.purpose = form['purpose'].data
                    test.method = form['method'].data

                    test.save()
                    return HttpResponseRedirect('payments.html')
            else:
                form = PaymentForm()
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
