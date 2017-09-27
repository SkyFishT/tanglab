# -*- coding: utf-8 -*"
from django.shortcuts import render
from students.models import Students
from forms import StuForm
# Create your views here.
#页面返回
def admin_page(request):
    return render(request, 'administration/admin_home.html')

def manage_about(request):
    return render(request,'administration/manage_about.html')

def manage_news(request):
    return render(request,'administration/manage_news.html')

def manage_achievement(request):
    return render(request,'administration/manage_achievement.html')

def manage_students(request):
    if request.method == 'POST':
        form = StuForm(request.POST)
        if form.is_valid():
            return render(request, 'administration/manage_students.html', {'StuForm':form})
    else:
        form = StuForm()
    return render(request,'administration/manage_students.html',{'StuForm':form})

def manage_experience(request):
    return render(request,'administration/manage_experience.html')

def manage_activity(request):
    return render(request,'administration/manage_activity.html')
#表单提交
def form_edit(request):
    #获取表单
    form = form_edit(request.POST or None)
    if form.is_valid():
        in_reading = form.cleaned_data['in_reading']
        enrollment = form.cleaned_data['enrollment']
        degree = form.cleaned_data['degree']
        name = form.cleaned_data['name']
        position = form.cleaned_data['position']
        company = form.cleaned_data['company']
        phone_number = form.cleaned_data['phone_number']
        Email = form.cleaned_data['Email']
        QQ = form.cleaned_data['QQ']
        stu = Students.objects(name=name)
