# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from students.models import Students
# Create your views here.

def in_reading(request):
    print(type(Students.objects))
    return render(request,'students/in_reading.html')

def graduates(request):
    return render(request,'students/graduates.html')