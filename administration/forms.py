# -*- coding: utf-8 -*"
from  django import forms
from students.models import Students


class StuForm(forms.Form):
    name = forms.CharField(max_length=20,label="姓名")
    in_reading = forms.CharField()
    enrollment = forms.IntegerField()
    degree = forms.CharField(max_length=20)
    position = forms.CharField(required="false")
    company = forms.CharField(required="false")
    phone_number = forms.IntegerField()
    Email = forms.CharField(max_length=100)
    QQ = forms.IntegerField()
    which_button = forms.CharField()