# -*- coding: utf-8 -*"
from django.shortcuts import render
from students.models import Students
from forms import StuForm


# Create your views here.
# 页面返回
def admin_page(request):
    return render(request, 'administration/admin_home.html')


def manage_about(request):
    return render(request, 'administration/manage_about.html')


def manage_news(request):
    return render(request, 'administration/manage_news.html')


def manage_achievement(request):
    return render(request, 'administration/manage_achievement.html')


def manage_students(request):
    print(1)
    stu = Students.objects.all()
    if request.method == 'POST':
        form = StuForm(request.POST)
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
            which_button = form.cleaned_data['which_button']
            stu = Students.objects.all()
            if (which_button == "delete"):
                Students.objects.filter(name=name).delete()
                return render(request, 'administration/manage_students.html', {'students': stu, 'StuForm': form})
            elif (which_button == "add"):
                Students(in_reading=in_reading, enrollment=enrollment, degree=degree, name=name, position=position,
                         company=company, phone_number=phone_number, Email=Email, QQ=QQ).save()
                return render(request, 'administration/manage_students.html', {'students': stu, 'StuForm': form})
            elif (which_button == "modify"):
                Students.objects(name=name).update(set__in_reading=in_reading, set__enrollment=enrollment, set__degree=degree, set__name=name, set__position=position,
                                                   set__company=company, set__phone_number=phone_number, set__Email=Email, set__QQ=QQ)
                return render(request, 'administration/manage_students.html', {'students': stu, 'StuForm': form})
        else:
            return render(request, 'administration/manage_students.html', {'students': stu, 'StuForm': form})

    else:
        form = StuForm()
    return render(request, 'administration/manage_students.html', {'students': stu, 'StuForm': form})


def manage_experience(request):
    return render(request, 'administration/manage_experience.html')


def manage_activity(request):
    return render(request, 'administration/manage_activity.html')
