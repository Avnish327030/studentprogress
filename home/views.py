from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

from django.contrib import messages
from home.models import Teacher
from home.form import TeacherForm,LoginForm
def home(request):
    if 'email_id' in request.session:
        teacher=Teacher.objects.all()

        return render(request,'home.html',{'teacher':teacher})
    else:
        messages.error(request, "Please !! login to your account ")
        return redirect('login')
def  register(request):
    if request.method=='POST':
        teacher_form = TeacherForm(request.POST or None, request.FILES or None)
        if teacher_form.is_valid():
            teacher_form.save()
            messages.success(request, "You have successfully registered ")
            return redirect('home')
        else:
            messages.error(request, "Registration failed !!")
            context = {'form': TeacherForm(request.POST),}
            return render(request, 'register.html', context)
    else:
        reg_form=TeacherForm()
        context={'form':reg_form}
        return render(request,'register.html',context)
def login(request):
    if 'email_id' in request.session:
        return redirect('student_detail')

    if request.method=='POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            teacher=Teacher.objects.get(teacher_email__exact=request.POST['teacher_email'])
            name=teacher.teacher_name
            request.session['name']=name
            request.session['email_id']=request.POST['teacher_email']
            request.session['id']=teacher.teacher_id
            messages.success(request,"SUCCESSFULLY LOGIN")
            return redirect('home')
        else:
            login_form=LoginForm(request.POST)
            context = {'form': login_form}
            return render(request, 'login.html', context)

    login_form=LoginForm()
    context={'form':login_form}
    return render(request,'login.html',context)


def logout(request):
    request.session.flush()
    messages.success(request,"You have successfully logout")
    return redirect('login')
