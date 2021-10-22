from django.contrib import admin
from app.models import Teacher,Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['idno','first_name','last_name','age','subject','contact_no','gender','date_of_birth','email','date_of_join','photo','salary']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['idno','first_name','last_name','age','subject','contact_no','gender','date_of_birth','email','marks','photo']


