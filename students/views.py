# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from students.models import Students
# Create your views here.

def in_reading(request):
    in_reading = Students.objects(in_reading="TRUE")
    print(type(Students.objects))
    return render(request,'students/in_reading.html',{'in_reading':in_reading})

def graduates(request):
    graduates = Students.objects(in_reading="FALSE")
    return render(request,'students/graduates.html',{'graduates':graduates})