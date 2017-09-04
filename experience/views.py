# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def acad_experience(request):
    return render(request,'experience/acad_experience.html')

def edu_experience(request):
    return render(request,'experience/edu_experience.html')