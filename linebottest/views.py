# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def callback(request):
    data = json.loads(request.body)
    result = data.get('result',False)
    if result:
        for i in result:
            content = i["content"]
            text = content["text"]
            print text

    return HttpResponse('')


