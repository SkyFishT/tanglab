# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def ent_activity(request):
    return render(request,'activity/ent_activity.html')

def acad_activity(request):
    return render(request,'activity/acad_activity.html')