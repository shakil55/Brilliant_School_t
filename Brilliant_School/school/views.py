from django.shortcuts import render
from .models import Notice, Teacher

def home(request):
    notices = Notice.objects.all().order_by('-date_posted')[:5]
    teachers = Teacher.objects.all()
    return render(request, 'school/home.html', {'notices': notices, 'teachers': teachers})
