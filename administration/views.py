from django.shortcuts import render

# Create your views here.
def admin_page(request):
    return render(request,'administration/admin_page.html')

def manage_about(request):
    return render(request,'administration/manage_about.html')

def manage_news(request):
    return render(request,'administration/manage_news.html')

def manage_achievement(request):
    return render(request,'administration/manage_achievement.html')

def manage_students(request):
    return render(request,'administration/manage_students.html')

def manage_experience(request):
    return render(request,'administration/manage_experience.html')

def manage_activity(request):
    return render(request,'administration/manage_activity.html')