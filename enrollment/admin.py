from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'last_name', 'first_name', 'course', 'year_level', 'section', 'enrollment_status')
    search_fields = ('student_id', 'last_name', 'first_name', 'course')
    list_filter = ('course', 'year_level', 'enrollment_status')