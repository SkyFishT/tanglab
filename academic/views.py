# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from academic.models import Theses,Patents
# Create your views here.

sub_menus = {'acad_achievement':"论文清单",'patents':"专利清单",'sci_project':"学术成果",'theses':"科研项目"}
def acad_achievement(request):
    return render(request, 'academic/acad_achievement.html',{'main_menu':"学术研究",'sub_menus':sub_menus,'position':"acad_achievement"})

def patents(request):
    patents = Patents.objects()
    return render(request,'academic/patents.html',{'main_menu':"学术研究",'sub_menus':sub_menus,'position':"patents",'patents':patents})

def sci_project(request):
    return render(request,'academic/sci_project.html',{'main_menu':"学术研究",'sub_menus':sub_menus,'position':"sci_project"})

def theses(request):
    theses = Theses.objects()
    return render(request,'academic/theses.html',{'main_menu':"学术研究",'sub_menus':sub_menus,'position':"theses",'theses':theses})
