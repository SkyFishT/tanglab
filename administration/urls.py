# -*- coding: utf-8 -*
from django.conf.urls import url
from views import *

urlpatterns = [
    #页面响应
    url(r'^$', admin_page, name='administration'),
    url(r'^manage_about', manage_about, name='manage_about'),
    url(r'^manage_news', manage_news, name='manage_news'),
    url(r'^manage_achievement', manage_achievement, name='manage_achievement'),
    url(r'^manage_students', manage_students, name='manage_students'),
    url(r'^manage_experience', manage_experience, name='manage_experience'),
    url(r'^manage_activity', manage_activity, name='manage_activity'),
    url(r'^manage_activity', manage_activity, name='manage_activity'),
    #form提交
    url(r'^form_edit',form_edit,name='form_edit'),
]
