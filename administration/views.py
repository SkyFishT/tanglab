from django.shortcuts import render
from students.models import Students

# Create your views here.
def admin_page(request):
    return render(request, 'administration/admin_home.html')

def manage_about(request):
    return render(request,'administration/manage_about.html')

def manage_news(request):
    return render(request,'administration/manage_news.html')

def manage_achievement(request):
    return render(request,'administration/manage_achievement.html')

def manage_students(request):
    stu = Students.objects.all()
    return render(request,'administration/manage_students.html',{'students':stu})

def manage_experience(request):
    return render(request,'administration/manage_experience.html')

def manage_activity(request):
    return render(request,'administration/manage_activity.html')