# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
# Create your models here.

class Students(Document):
    in_reading = StringField(max_length=5)
    enrollment = IntField()
    degree = StringField(max_length=20)
    name = StringField(max_length=20)
    position = StringField()
    company = StringField()
    phone_number = LongField()
    Email = StringField(max_length=100)
    QQ = LongField()