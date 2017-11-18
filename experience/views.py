# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from experience.models import Experience

# Create your views here.
sub_menus = {'acad_experience':"学术心得转载",'edu_experience':"人才培养心得转载"}
def acad_experience(request):
    experience = Experience.objects(type="acad_experience")
    return render(request,'experience/acad_experience.html',{"main_menu":"他山之石","sub_menus":sub_menus,'position':"acad_experience",'experience':experience})

def edu_experience(request):
    experience = Experience.objects(type="edu_experience")
    return render(request,'experience/edu_experience.html',{"main_menu":"他山之石","sub_menus":sub_menus,'position':"edu_experience",'experience':experience})