# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
sub_menus = {'achievement':"最新成果",'information':"学术资讯"}
def achievement(request):
    return render(request,'news/achievement.html',{'main_menu':"最新消息","sub_menus":sub_menus,'position':"achievement"})

def information(request):
    return render(request,'news/information.html',{'main_menu':"最新消息","sub_menus":sub_menus,'position':"information"})
