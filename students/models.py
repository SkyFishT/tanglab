# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
# Create your models here.

class Students(Document):
    name = StringField(max_length=20)
    in_school = BooleanField()