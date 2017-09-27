from django.conf.urls import url
from views import *

urlpatterns = [
url(r'^acad_experience', acad_experience, name='acad_experience'),
    url(r'^edu_experience', edu_experience, name='edu_experience'),
]