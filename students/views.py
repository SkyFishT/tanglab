# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def in_reading(request):
    return render(request,'students/in_reading.html')

def graduates(request):
    return render(request,'students/graduates.html')