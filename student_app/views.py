from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# READ: View all student records
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_app/student_list.html', {'students': students})

# CREATE: Add a new student record
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')
        Student.objects.create(name=name, email=email, age=age, course=course)
        return redirect('student_list')
    return render(request, 'student_app/student_form.html')

# UPDATE: Modify existing student details
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')
    return render(request, 'student_app/student_form.html', {'student': student})

# DELETE: Remove a student record
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')