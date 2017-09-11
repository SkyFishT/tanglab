# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
sub_menus = {'about':"概况",'members':"团队人员",'contact':"联系我们"}

#概况
def about(request):
    return render(request, 'about/about.html',{'main_menu':"关于我们",'sub_menus':sub_menus,'position':"about"})

#团队人员
def members(request):
    return render(request, 'about/members.html',{'main_menu':"关于我们",'sub_menus':sub_menus,'position':"members"})

#联系我们
def contact(request):
    return render(request, 'about/contact.html',{'main_menu':"关于我们",'sub_menus':sub_menus,'position':"contact"})