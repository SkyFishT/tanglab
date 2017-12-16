# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from home.models import Messages,Achievements
# Create your views here.

def index(request):
    home_msgs = Messages.objects()
    home_achieve = Achievements.objects()
    return render(request,'home/index.html',{'home_msgs':home_msgs,'home_achieve':home_achieve})