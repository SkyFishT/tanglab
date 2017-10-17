# -*- coding: utf-8 -*"
from  django import forms
from students.models import Students


class StuForm(forms.Form):
    name = forms.CharField(max_length=20,label="姓名")
    in_reading = forms.ChoiceField(choices=(("TRUE","在读"),("FALSE","离校")))
    enrollment = forms.IntegerField(min_value=2002,max_value=2500)
    degree = forms.ChoiceField(choices=(("master","硕士"),("doctor","博士")))
    position = forms.CharField(required="false")
    company = forms.CharField(required="false")
    phone_number = forms.IntegerField(min_value=10000000000,max_value=19999999999,required=False,error_messages={'invalid':u'请输入正确的电话号码'})
    Email = forms.EmailField(max_length=100)
    QQ = forms.IntegerField()
    which_button = forms.CharField()