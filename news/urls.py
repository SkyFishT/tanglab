from django.conf.urls import url
from views import *

urlpatterns = [
url(r'^achievement', achievement, name='achievement'),
    url(r'^information', information, name='information'),
]