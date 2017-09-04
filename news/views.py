# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def achievement(request):
    return render(request,'news/achievement.html')

def information(request):
    return render(request,'news/information.html')
