from django.shortcuts import get_object_or_404, render
from .models import Student, SubjectMarks

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    subject_marks = SubjectMarks.objects.filter(student=student).first()
    context = {
        'student': student,
        'subject_marks': subject_marks,
    }
    return render(request, 'studetails.html', context)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

