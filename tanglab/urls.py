# -*- coding: utf-8 -*"
""""tanglab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from home import views as home_views
from about import views as about_views
from news import views as news_views
from academic import views as academic_vews
from students import views as studenst_views
from experience import views as experience_views
from activity import views as activity_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_views.index),
    #关于我们
    url(r'^about',about_views.about,name='about'),
    url(r'^contact',about_views.contact,name='contact'),
    url(r'^members',about_views.members,name='members'),
    #最新消息
    url(r'^achievement',news_views.achievement,name='achievement'),
    url(r'^information',news_views.information,name='information'),
    #学术研究
    url(r'^acad_achievement',academic_vews.acad_achievement,name='acad_achievement'),
    url(r'^patents',academic_vews.patents,name='patents'),
    url(r'^theses',academic_vews.theses,name='theses'),
    url(r'^sci_project',academic_vews.sci_project,name='sci_project'),
    #教学与人才培养
    url(r'^in_reading',studenst_views.in_reading,name='in_reading'),
    url(r'^graduates',studenst_views.graduates,name='graduates'),
    #他山之石
    url(r'^acad_experience',experience_views.acad_experience,name='acad_experience'),
    url(r'^edu_experience',experience_views.edu_experience,name='edu_experience'),
    #校园生活
    url(r'^ent_activity',activity_views.ent_activity,name='ent_activity'),
    url(r'^acad_activity',activity_views.acad_activity,name='acad_activity'),
]
