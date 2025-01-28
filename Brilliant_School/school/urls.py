from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('notices/', views.notice_board, name='notices_board'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    # path('admin-dashboard/add_student/', views.add_student, name='add_student'),
    # path('admin-dashboard/view-students/', views.view_students, name='view_students'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('history/', views.history, name='history'),
    path('mission-vision/', views.mission_vision, name='mission-vision'),
    path('facilities/', facilities_view, name='facilities'),
    path('result/',views.result_view,name='result'),
    path('admission_information/',views.admission_information, name='addmission_info'),
    path('contact/', views.contact_us, name='contact_us'),
    path('add-student/', views.add_student, name='add_student'),
    # path('add-multiple-students/', views.add_multiple_students, name='add_multiple_students'),
    # path('students/', views.student_list, name='student_list'),
    path('students/', views.view_students, name='view_students'),
    path('view_students/', views.all_students, name='all_students'),

    path('exam-schedule/', views.exam_schedule, name='exam_schedule'),
    path('news/', views.news, name='news'),
    path('routine/', views.routine, name='routine'),
    path('gallery/', views.gallery, name='gallery'),
    
    path('students/<str:student_class>/<str:section>/', views.student_list, name='student_list'),
    path('attendance/<str:student_class>/<str:section>/', views.take_attendance, name='take_attendance'),

    path('classes/', views.class_list, name='class_list'),
    path('classes/<str:student_class>/sections/', views.section_list, name='section_list'),
    path('classes/<str:student_class>/sections/<str:section>/students/', views.student_list, name='student_list'),
    path('classes/<str:student_class>/sections/<str:section>/attendance/', views.take_attendance, name='take_attendance'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
