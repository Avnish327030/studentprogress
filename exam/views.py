from django.shortcuts import render,redirect
from home.models import Teacher
from django.contrib import messages
from student.models import Student
from exam.models import Exam
from exam.form import ExamForm
# Create your views here.
def home(request):
    if 'email_id' in request.session:
        teacher_id = request.session['id']
        exam = Exam.objects.filter(teacher_id__exact=teacher_id)
        if request.method == 'POST':
            exam_form = ExamForm(request.POST or None)
            if exam_form.is_valid():
                exam_form.save()
                messages.success(request, "EXAM DETAIL ADDED SUCCESSFULLY")
                return redirect('exam')
            else:
                messages.error(request, "ERROR OCCURED !!")
                teacher = Teacher.objects.get(teacher_id__exact=teacher_id)
                context = {'form': ExamForm(request.POST), 'teacher': teacher,'exam':exam}
                return render(request, 'exam.html', context)
        exam_form = ExamForm(initial={'teacher_id': teacher_id, })
        teacher = Teacher.objects.get(teacher_id__exact=teacher_id)
        context = {'form': exam_form, 'teacher': teacher,'exam':exam}
        return render(request, 'exam.html', context)
    else:
        messages.error(request, "Please !! login to your account ")
        return redirect('login')
