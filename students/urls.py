from django.conf.urls import url
from students.views import *

urlpatterns = [
url(r'^in_reading', in_reading, name='in_reading'),
    url(r'^graduates', graduates, name='graduates'),
]