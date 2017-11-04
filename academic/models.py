# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mongoengine import *
from django.db import models

# Create your models here.
class Theses(Document):
    time = IntField()
    name = StringField(max_length=100)
    authors = StringField(max_length=50)
    rank = IntField()
    journal = StringField(max_length=100)
    publication = StringField(max_length=20)
    type = StringField(max_length=20)
    _2010IF = IntField()
    _2015IF = IntField()
    _5YIF = IntField()
    foreign = StringField(max_length=20)
    remark = StringField(max_length=100)
    inland = StringField(max_length=100)
    SCI = IntField()
    EI = IntField()
    ISTP = IntField()
    citing = IntField()
    other_citing = IntField()

class Patents(Document):
    time = StringField(max_length=50)
    status = StringField(max_length=20)
    patent_name = StringField(max_length=100)
    inventor = StringField(max_length=50)
    patent_number= StringField(max_length=50)
    position = StringField(max_length=50)
    patentee = StringField(max_length=50)