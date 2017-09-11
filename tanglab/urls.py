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
from administration import views as admin_views

urlpatterns = [
    url(r'^administration/', admin.site.urls),
    url(r'^$', home_views.index, name='home'),
    # 关于我们
    url(r'^about/about', about_views.about, name='about'),
    url(r'^about/contact', about_views.contact, name='contact'),
    url(r'^about/members', about_views.members, name='members'),
    # 最新消息
    url(r'^news/achievement', news_views.achievement, name='achievement'),
    url(r'^news/information', news_views.information, name='information'),
    # 学术研究
    url(r'^academic/acad_achievement', academic_vews.acad_achievement, name='acad_achievement'),
    url(r'^academic/patents', academic_vews.patents, name='patents'),
    url(r'^academic/theses', academic_vews.theses, name='theses'),
    url(r'^academic/sci_project', academic_vews.sci_project, name='sci_project'),
    # 教学与人才培养
    url(r'^students/in_reading', studenst_views.in_reading, name='in_reading'),
    url(r'^students/graduates', studenst_views.graduates, name='graduates'),
    # 他山之石
    url(r'^experience/acad_experience', experience_views.acad_experience, name='acad_experience'),
    url(r'^experience/edu_experience', experience_views.edu_experience, name='edu_experience'),
    # 校园生活
    url(r'^activity/ent_activity', activity_views.ent_activity, name='ent_activity'),
    url(r'^activity/acad_activity', activity_views.acad_activity, name='acad_activity'),
    # 管理界面
    url(r'^admin$', admin_views.admin_page, name='administration'),
    url(r'^admin/manage_about', admin_views.manage_about, name='manage_about'),
    url(r'^admin/manage_news', admin_views.manage_news, name='manage_news'),
    url(r'^admin/manage_achievement', admin_views.manage_achievement, name='manage_achievement'),
    url(r'^admin/manage_students', admin_views.manage_students, name='manage_students'),
    url(r'^admin/manage_experience', admin_views.manage_experience, name='manage_experience'),
    url(r'^admin/manage_activity', admin_views.manage_activity, name='manage_activity'),
]
