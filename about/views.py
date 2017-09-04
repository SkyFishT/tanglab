# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#概况
def about(request):
    return render(request, 'about/about.html')

#团队人员
def contact(request):
    return render(request, 'about/contact.html')

#联系我们
def members(request):
    return render(request, 'about/members.html')