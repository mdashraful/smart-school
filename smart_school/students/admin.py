from django.contrib import admin
from students.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_num', 'fname', 'lname', 'email', 'phone', 'gender', 'dob', 'created_at')
    search_fields = ('fname', 'lname', 'email', 'phone', 'reg_num')
