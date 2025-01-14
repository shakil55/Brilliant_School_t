from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Student, Teacher, Notice
from .forms import StudentForm, TeacherForm, NoticeForm

def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    notices = Notice.objects.order_by('-date_posted')[:5]
    return render(request, 'school/admin_dashboard.html', {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'notices': notices
    })

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'শিক্ষার্থী সফলভাবে যোগ করা হয়েছে!')
            return redirect('add_student')
    else:
        form = StudentForm()
    return render(request, 'school/add_student.html', {'form': form})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'শিক্ষক সফলভাবে যোগ করা হয়েছে!')
            return redirect('add_teacher')
    else:
        form = TeacherForm()
    return render(request, 'school/add_teacher.html', {'form': form})

def manage_notices(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'নোটিশ সফলভাবে তৈরি হয়েছে!')
            return redirect('manage_notices')
    else:
        form = NoticeForm()
    notices = Notice.objects.order_by('-date_posted')
    return render(request, 'school/manage_notices.html', {'form': form, 'notices': notices})

def home(request):
    notices = Notice.objects.order_by('-date_posted')[:5]
    teachers = Teacher.objects.all()
    return render(request, 'school/home.html', {'notices': notices, 'teachers': teachers})

def notice_board(request):
    notices = Notice.objects.order_by('-date_posted')
    return render(request, 'school/notice.html', {'notices': notices})

def view_students(request):
    # Group students by class dynamically
    students_by_class = {}
    class_choices = ['প্লে', '১ম', '২য়', '৩য়', '৪র্থ', '৫ম', '৬ষ্ঠ', '৭ম', '৮ম', '৯ম', '১০ম']

    for student_class in class_choices:
        students = Student.objects.filter(student_class=student_class)
        if students.exists():
            students_by_class[student_class] = students

    return render(request, 'school/view_students.html', {'students_by_class': students_by_class})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'school/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'school/teacher_details.html', {'teacher': teacher})

# navbar link

def history(request):
    return render(request, 'school/history.html')

def mission_vision(request):
    return render(request, 'school/mission_vision.html')


def facilities_view(request):
    return render(request, 'school/facilities.html')

def result_view(request):
    return render(request, 'school/result.html')

def admission_information(request):
    return render(request, 'school/addmission_info.html' )

def contact_us(request):
    return render(request, 'school/contact_us.html')


