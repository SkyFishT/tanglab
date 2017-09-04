# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def acad_achievement(request):
    return render(request, 'academic/acad_achievement.html')

def patents(request):
    return render(request,'academic/patents.html')

def sci_project(request):
    return render(request,'academic/sci_project.html')

def theses(request):
    return render(request,'academic/theses.html')
