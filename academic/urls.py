from django.conf.urls import url
from academic.views import *

urlpatterns = [
    url(r'^acad_achievement', acad_achievement, name='acad_achievement'),
    url(r'^patents', patents, name='patents'),
    url(r'^theses', theses, name='theses'),
    url(r'^sci_project', sci_project, name='sci_project'),
]