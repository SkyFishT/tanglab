# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

def index(request):
    home_msg = "欢迎访问Tanglab网站"
    home_msgs = ["新闻1","新闻2"]
    return render(request,'home/index.html',{'home_msg':home_msg,'home_msgs':home_msgs})