# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
sub_menus = {'ent_activity':"文娱活动剪影",'acad_activity':"学术活动剪影"}
def ent_activity(request):
    return render(request,'activity/ent_activity.html',{"main_menu":"校园生活","sub_menus":sub_menus,'position':"ent_activity"})

def acad_activity(request):
    return render(request,'activity/acad_activity.html',{"main_menu":"校园生活","sub_menus":sub_menus,'position':"acad_activity"})