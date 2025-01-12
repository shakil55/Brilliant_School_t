from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('notices/', views.notice_board, name='notices_board'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('admin-dashboard/add_student/', views.add_student, name='add_student'),
    path('admin-dashboard/view-students/', views.view_students, name='view_students'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('history/', views.history, name='history'),
    path('mission-vision/', views.mission_vision, name='mission-vision'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
