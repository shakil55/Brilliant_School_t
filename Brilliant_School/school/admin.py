
from django.contrib import admin
from .models import Teacher, Notice, Student

admin.site.register(Teacher)
admin.site.register(Student)
# admin.site.register(Notice)

@admin.register(Notice)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'file')
    list_filter = ('date_posted',)
    search_fields = ('title',)

# Register your models here.
