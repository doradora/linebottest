# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import requests


# Create your views here.
@csrf_exempt
def callback(request):
    data = json.loads(request.body)
    result = data.get('result',False)
    if result:
        for i in result:
            content = i["content"]
            text = content["text"]
            user = content["from"]
            print user,"<====from"
            sendTextMessage([user], "幹死你")
    return HttpResponse('')



def sendTextMessage(sender, text):
    headers = {
        'Content-type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': "1478429960",
        'X-Line-ChannelSecret': "4a559935218f6763166835eb9b5582a5",
        'X-Line-Trusted-User-With-ACL': "u8294a91bd4eaff7cdcca0aaeb1210ce4",
    }
    data = {
        "to":sender,
        "toChannel":1383378250,
        "eventType":"138311608800106203",
        "content":{}
    }
    content = data['content']
    content["contentType"]=1,
    content["toType"] = 1,
    content["text"] = text
    print data,"<====data"
    r = requests.post("https://trialbot-api.line.me", data=data, headers=headers)
    print r.content,"<====content"
  # const data = {
  #   to: [sender],
  #   toChannel: 1383378250,
  #   eventType: '138311608800106203',
  #   content: {
  #     contentType: 1,
  #     toType: 1,
  #     text: text
  #   }
  # };
