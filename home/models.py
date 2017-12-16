# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *

from django.db import models

# Create your models here.
class Messages(Document):
    msg = StringField(max_length=500)

class Achievements(Document):
    achieve = StringField(max_length=500)