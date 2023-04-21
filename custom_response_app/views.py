from django.shortcuts import render

from django.http import HttpResponse
import datetime

def index(request):
    current_datetime = datetime.datetime.now()  
    html = "Current Date and Time Value:%s" % current_datetime
    return HttpResponse(html)

