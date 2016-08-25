# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def callback(request):
    data = request.POST
    print data
    return HttpResponse('')


