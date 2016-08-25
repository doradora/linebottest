# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def callback(request):
    data = request.POST
    print data


