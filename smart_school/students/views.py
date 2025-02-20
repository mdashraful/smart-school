from django.shortcuts import render, HttpResponse
from .models import Student
from .forms import StudentForm

# List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_update(request, pk):
    return HttpResponse("Edit")

def student_delete(request, pk):
    return HttpResponse("Delete")