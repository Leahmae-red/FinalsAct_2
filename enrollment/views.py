from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by('last_name')
    return render(request, 'enrollment/student_list.html', {'students': students})

def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'enrollment/student_profile.html', {'student': student})