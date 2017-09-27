from  django import forms
from students.models import Students


class StuForm(forms.Form):
    name = forms.CharField(max_length=20)
    in_reading = forms.CharField(max_length=5)
    enrollment = forms.IntegerField()
    degree = forms.CharField(max_length=20)
    position = forms.CharField()
    company = forms.CharField()
    phone_number = forms.IntegerField()
    Email = forms.CharField(max_length=100)
    QQ = forms.IntegerField()