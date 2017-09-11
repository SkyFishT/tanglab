# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
sub_menus = {'acad_experience':"学术心得转载",'edu_experience':"人才培养心得转载"}
def acad_experience(request):
    return render(request,'experience/acad_experience.html',{"main_menu":"他山之石","sub_menus":sub_menus,'position':"acad_experience"})

def edu_experience(request):
    return render(request,'experience/edu_experience.html',{"main_menu":"他山之石","sub_menus":sub_menus,'position':"edu_experience"})