# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.

class Experience(Document):
    name = StringField(max_length=100)
    type = StringField(max_length=20)