from django.conf.urls import url
from about.views import *

urlpatterns = [
url(r'^about/', about, name='about'),
    url(r'^about/', contact, name='contact'),
    url(r'^about/', members, name='members'),
]