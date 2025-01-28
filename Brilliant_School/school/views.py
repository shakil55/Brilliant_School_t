from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from .models import Student, Teacher, Notice , CLASS_CHOICES, Attendance
from .forms import StudentForm, TeacherForm, NoticeForm 
from django.forms import modelform_factory, modelformset_factory
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator



def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    notices = Notice.objects.order_by('-date_posted')[:5]
    return render(request, 'school/admin_dashboard.html', {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'notices': notices
    })


# Form for adding a single student
StudentForm = modelform_factory(Student, exclude=[])

# Formset for adding multiple students
StudentFormSet = modelformset_factory(Student, form=StudentForm, extra=5)

# View for adding students
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to a student list view
    else:
        form = StudentForm()
    return render(request, 'school/add_student.html', {'form': form})



def class_list(request):
    """Display all available classes."""
    classes = sorted(set(Student.objects.values_list('student_class', flat=True)))
    return render(request, 'school/class_list.html', {'classes': classes})

def section_list(request, student_class):
    """Display sections for a specific class."""
    sections = sorted(set(Student.objects.filter(student_class=student_class).values_list('section', flat=True)))
    return render(request, 'school/section_list.html', {'sections': sections, 'student_class': student_class})

def student_list(request, student_class, section):
  
    try:
        # Retrieve students filtered by class and section, ordered by roll number
        students = Student.objects.filter(
            student_class=student_class,
            section=section
        ).order_by('roll_number')

        # Render the template with the student list
        return render(request, 'school/student_list.html', {
            'students': students,
            'student_class': student_class,
            'section': section,
        })

    except Student.DoesNotExist:
        # Handle case where no students are found
        return render(request, 'school/student_list.html', {
            'students': [],
            'student_class': student_class,
            'section': section,
            'error_message': 'No students found for this class and section.',
        })
    
def take_attendance(request, student_class, section):
    """Take attendance for students in a specific class and section."""
    students = Student.objects.filter(student_class=student_class, section=section).order_by('roll_number')
    if request.method == "POST":
        attendance_data = request.POST.dict()
        for student in students:
            status = attendance_data.get(f"status_{student.id}", "Absent")
            Attendance.objects.create(student=student, status=status)
        return JsonResponse({'success': True, 'redirect_url': reverse('class_list')})

    return render(request, 'school/take_attendance.html', {'students': students, 'student_class': student_class, 'section': section})


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

def exam_schedule(request):
    return render(request, 'school/exam_schedule.html')

def news(request):
    return render(request, 'school/news.html')

def routine(request):
    return render(request, 'school/routine.html')

def gallery(request):
    return render(request, 'school/gallery.html')




def view_students(request):
    # Your view logic here
    return render(request, 'students.html')


def all_students(request):
    students = Student.objects.all()
    student_class = request.GET.get('class', '')
    section = request.GET.get('section', '')
    search_query = request.GET.get('search', '')

    if student_class:
        students = students.filter(student_class=student_class)
    if section:
        students = students.filter(section=section)
    if search_query:
        students = students.filter(name__icontains=search_query)

    paginator = Paginator(students, 5)  # Show 10 students per page
    page_number = request.GET.get('page')
    students_page = paginator.get_page(page_number)
    
    students_data = [
        ('প্লে', 'প্লে', 120),
        ('নার্সারি', 'নার্সারি', 135),
        ('প্রথম', 'প্রথম', 200),
        ('দ্বিতীয়', 'দ্বিতীয়', 180),
        ('তৃতীয়', 'তৃতীয়', 160),
        ('চতুর্থ', 'চতুর্থ', 150),
        ('পঞ্চম', 'পঞ্চম', 140),
        ('ষষ্ঠ', 'ষষ্ঠ', 130),
        ('সপ্তম', 'সপ্তম', 125),
        ('অষ্টম', 'অষ্টম', 115),
        ('নবম', 'নবম', 110),
        ('দশম', 'দশম', 100),
    ]
    context = {
        'students': students_page,
        'class_choices': Student._meta.get_field('student_class').choices,
        'section_choices': Student._meta.get_field('section').choices,
        'search_query': search_query,
        'students_data': students_data,  # Pass statistics to the template
    }
    return render(request, 'school/all_students.html', context)
