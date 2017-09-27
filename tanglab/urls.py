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

from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views

urlpatterns = [
    url(r'^administration/', admin.site.urls),
    url(r'^$', home_views.index, name='home'),
    # 关于我们
    url(r'^about/about', include("about.urls")),
    # 最新消息
    url(r'^news/', include("news.urls")),
    # 学术研究
    url(r'^academic/', include("academic.urls")),
    # 教学与人才培养
    url(r'^students/', include("students.urls")),
    # 他山之石
    url(r'^experience/', include("experience.urls")),
    # 校园生活
    url(r'^activity/', include("activity.urls")),
    # 管理界面
    url(r'^admin/', include("administration.urls")),
]
