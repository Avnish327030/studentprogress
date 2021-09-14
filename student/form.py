import datetime
from urllib import request
from passlib.hash import pbkdf2_sha256
from django import forms
from home.models import Teacher
from student.models import Student
from django.db.models import Max
from exam.models import Exam
from student.models import StudentMarks
class StudentForm(forms.ModelForm):
    teacher_id=forms.CharField(widget=forms.TextInput(attrs={'name':'teacher_id','class':'form-control','readonly':'true','type':'hidden'}),label="TEACHER ID")
    fname=forms.CharField(widget=forms.TextInput(attrs={'name':'fname','placeholder':'FIRST NAME','class':'form-control'}),required=True,label="FIRST NAME")
    lname = forms.CharField(widget=forms.TextInput(attrs={'name': 'lname', 'placeholder': 'LAST NAME','class':'form-control'}), required=True,label="LAST NAME")
    img = forms.ImageField( widget=forms.FileInput(attrs={'name': 'image', 'class': 'inputfile', 'onchange': 'readURL(this);'}), label="PROFILE")
    rollno=forms.IntegerField(widget=forms.NumberInput(attrs={'type':'hidden','name':'roll_no',}),required=False,label="ROLL NUMBER")
    std=forms.ChoiceField(widget=forms.Select(attrs={'name':'std','placeholder':'STANDARD','class':'form-control'}),required=True,label="STANDARD",choices=([('','<--select standard-->'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]))
    medium=forms.CharField(widget=forms.TextInput(attrs={'name':'medium','placeholder':'MEDIUM','class':'form-control'}),required=True,label="MEDIUM")
    school_name=forms.CharField(widget=forms.Textarea(attrs={'name':'school_name','placeholder':'SCHOOL NAME','class':'form-control','rows':'5',}),required=True,label="SCHOOL NAME")
    class Meta:
        model=Student
        fields=(
            'teacher_id',
            'fname',
            'lname',
            'img',
            'rollno',
            'std',
            'medium',
            'school_name',


        )

    def clean(self):
        t_id = self.cleaned_data['teacher_id']

        self.cleaned_data['teacher_id'] = Teacher.objects.get(teacher_id=t_id)
        std=self.cleaned_data['std']
        stud = Student.objects.filter(teacher_id__exact=t_id,std__exact=std)
        if stud.count() == 0:
            self.cleaned_data['rollno'] = 1
        else:
            stud = stud.aggregate(Max('rollno'))
            rollno = stud.get('rollno__max')
            self.cleaned_data['rollno']=rollno+1
        return self.cleaned_data



class StudentMarksForm(forms.ModelForm):
    class Meta:
        model=StudentMarks
        fields=(
            'exam_id',
            'student_id',
            'teacher_id',
            'obtain_mark',

        )