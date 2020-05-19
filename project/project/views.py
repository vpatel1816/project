# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render

    
def home(request):
    #return HttpResponse("in Home page")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("im in about page")
    return render(request,'about.html')
