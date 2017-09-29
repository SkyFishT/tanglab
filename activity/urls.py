from django.conf.urls import url
from activity.views import *

urlpatterns = [
url(r'^ent_activity', ent_activity, name='ent_activity'),
    url(r'^acad_activity', acad_activity, name='acad_activity'),
]