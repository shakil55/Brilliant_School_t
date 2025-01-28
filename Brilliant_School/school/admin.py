from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path, reverse
import pandas as pd
from django import forms
from django.utils.html import format_html
from django.contrib import messages
from .models import Student, Teacher, Notice, Attendance

admin.site.register(Teacher)

@admin.register(Notice)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'file')
    list_filter = ('date_posted',)
    search_fields = ('title',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status', 'student__student_class', 'student__section')

class StudentUploadForm(forms.Form):
    file = forms.FileField(label="Upload CSV/Excel")

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_class', 'roll_number')
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload/', self.admin_site.admin_view(self.upload_students), name="upload_students"),
        ]
        return custom_urls + urls

    def upload_students(self, request):
        if request.method == 'POST':
            form = StudentUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                try:
                    if file.name.endswith('.csv'):
                        df = pd.read_csv(file)
                    elif file.name.endswith('.xlsx'):
                        df = pd.read_excel(file)
                    else:
                        self.message_user(request, "Invalid file format. Please upload a CSV or Excel file.", level='error')
                        return redirect("admin:upload_students")

                    for _, row in df.iterrows():
                        Student.objects.update_or_create(
                            student_class=row['student_class'],
                            section=row['section'],
                            roll_number=row['roll_number'],
                            defaults=row.to_dict()
                        )

                    self.message_user(request, "Students uploaded successfully.", level='success')
                    return redirect("..")

                except Exception as e:
                    self.message_user(request, f"Error processing file: {e}", level='error')
                    return redirect("admin:upload_students")
        else:
            form = StudentUploadForm()

        context = {
            'form': form,
            'opts': self.model._meta,
            'title': "Upload Students",
        }
        return render(request, 'admin/upload_csv.html', context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        upload_url = reverse('admin:upload_students')
        extra_context['upload_link'] = format_html('<a class="button" href="{}">Upload CSV/Excel</a>', upload_url)
        return super().add_view(request, form_url, extra_context)

admin.site.register(Student, StudentAdmin)


from .models import SMSMessage
from .utils import send_sms

class SMSMessageAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'message', 'sent_at', 'status')
    actions = ['send_selected_sms']

    def send_selected_sms(self, request, queryset):
        for sms in queryset:
            response = send_sms(sms.phone_number, sms.message)
            if response.get('error'):
                sms.status = 'Failed'
            else:
                sms.status = 'Sent'
            sms.save()
        self.message_user(request, "Selected SMS messages have been sent.")
    
    send_selected_sms.short_description = "Send selected SMS"

admin.site.register(SMSMessage, SMSMessageAdmin)

