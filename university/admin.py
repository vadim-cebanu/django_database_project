from django.contrib import admin
from .models import Student, StudentIDCard, Professor, Semester, Course, CourseDescription

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'enrollment_date']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['enrollment_date']

@admin.register(StudentIDCard)
class StudentIDCardAdmin(admin.ModelAdmin):
    list_display = ['card_number', 'student', 'issue_date', 'expiry_date']
    search_fields = ['card_number', 'student__first_name', 'student__last_name']
    list_filter = ['issue_date', 'expiry_date']

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'department']
    search_fields = ['first_name', 'last_name', 'email', 'department']
    list_filter = ['department']

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    search_fields = ['name']
    list_filter = ['start_date', 'end_date']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'professor', 'semester']
    search_fields = ['code', 'name', 'professor__first_name', 'professor__last_name']
    list_filter = ['semester', 'professor']
    filter_horizontal = ['students']

@admin.register(CourseDescription)
class CourseDescriptionAdmin(admin.ModelAdmin):
    list_display = ['course', 'objectives']
    search_fields = ['course__name', 'course__code', 'objectives']
