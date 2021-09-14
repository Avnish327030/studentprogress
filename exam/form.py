import datetime
from urllib import request
from passlib.hash import pbkdf2_sha256
from django import forms
from home.models import Teacher
from exam.models import Exam
class ExamForm(forms.ModelForm):
    teacher_id = forms.CharField(
        widget=forms.TextInput(attrs={'name': 'teacher_id', 'class': 'form-control', 'readonly': 'true','type':'hidden'}),
        label="TEACHER ID")
    exam_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'name': 'exam_date', 'placeholder': 'DATE-OF-EXAM', 'type': 'date', }),
        required=True, label="EXAM DATE")
    std = forms.ChoiceField(
        widget=forms.Select(attrs={'name': 'std', 'placeholder': 'STANDARD', 'class': 'form-control'}), required=True,
        label="STANDARD", choices=(
        [('','<--select standard-->'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10')]))
    subject = forms.ChoiceField(
        widget=forms.Select(attrs={'name': 'subject', 'placeholder': 'SUBJECT', 'class': 'form-control'}), required=True,
        label="SUBJECT", choices=(
        [('','<--select subject-->'),('HINDI', 'HINDI'), ('MARATHI', 'MARATHI'), ('HISTORY', 'HISTORY'), ('GEOGRAPHY', 'GEOGRAPHY'), ('MATH', 'MATH'), ('SCIENCE', 'SCIENCE')]))
    chapter = forms.CharField(
        widget=forms.TextInput(attrs={'name': 'chapter', 'class': 'form-control', 'placeholder': 'CHAPTER'}),
        label="CHAPTER")
    total_mark = forms.IntegerField(
        widget=forms.NumberInput(attrs={'name': 'total_marks', 'class': 'form-control', 'placeholder': 'TOTAL MARKS'}),
        label="TOTAL MARKS")

    class Meta:
        model=Exam
        fields=(
            'teacher_id',
            'exam_date',
            'std',
            'subject',
            'chapter',
            'total_mark'

        )

    def clean(self):
        t_id = self.cleaned_data['teacher_id']
        std=self.cleaned_data['std']
        self.cleaned_data['teacher_id'] = Teacher.objects.get(teacher_id=t_id)
        return self.cleaned_data
