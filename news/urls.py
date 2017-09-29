from django.conf.urls import url
from news.views import *

urlpatterns = [
url(r'^achievement', achievement, name='achievement'),
    url(r'^information', information, name='information'),
]