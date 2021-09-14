import datetime
from urllib import request
from passlib.hash import pbkdf2_sha256
from django import forms
from home.models import Teacher
class TeacherForm(forms.ModelForm):
    teacher_email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'EMAIL'}),label="EMAIL")
    teacher_name=forms.CharField(widget=forms.TextInput(attrs={'name':'teacher_name','class':'form-control','placeholder':'TEACHER NAME'}),label="TEACHER NAME")
    teacher_pass=forms.CharField(widget=forms.PasswordInput(attrs={'name':'password','class':'form-control','placeholder':'PASSWORD'}),label="PASSWORD")
    teacher_cpass = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'cpassword', 'class': 'form-control', 'placeholder': 'CONFIRM PASSWORD'}),label="CONFIRM PASSWORD")
    phone_no=forms.IntegerField(widget=forms.NumberInput(attrs={'name':'phone_no','class':'form-control','placeholder':'PHONE NO'}),label="MOBILE NO")
    img = forms.ImageField( widget=forms.FileInput(attrs={'name': 'image', 'class': 'inputfile','onchange':'readURL(this);'}), label="PROFILE")

    class Meta:
        model=Teacher
        fields=(
            'teacher_name',
            'teacher_pass',
            'teacher_cpass',
            'phone_no',
            'teacher_email',
            'img',
        )


    def clean(self):
        t_name=self.cleaned_data['teacher_name']
        t_pass=self.cleaned_data['teacher_pass']
        t_cpass=self.cleaned_data['teacher_cpass']
        t_mail=self.cleaned_data['teacher_email']
        t_phone=self.cleaned_data['phone_no']
        res=Teacher.objects.filter(teacher_email__exact=t_mail)
        if res.count()!=0:
            raise forms.ValidationError('EMAIL ALREADY USED')
        self.cleaned_data['teacher_pass'] = pbkdf2_sha256.using(rounds=8000, salt_size=10).hash(t_pass)
        if not pbkdf2_sha256.verify(t_cpass,self.cleaned_data['teacher_pass']):
            raise forms.ValidationError('PASSWORD NOT MATCHED')
        self.cleaned_data['teacher_cpass']=self.cleaned_data['teacher_pass']
        res=Teacher.objects.filter(phone_no__exact=t_phone)
        if res.count()!=0:
            raise forms.ValidationError('PHONE NUMBER ALREADY USED')
        return self.cleaned_data
class LoginForm(forms.ModelForm):
    teacher_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'name': 'email', 'class': 'form-control', 'placeholder': 'EMAIL'}),
        label="EMAIL")
    teacher_pass = forms.CharField(
        widget=forms.PasswordInput(attrs={'name': 'password', 'class': 'form-control', 'placeholder': 'PASSWORD'}),
        label="PASSWORD")

    class Meta:
        model = Teacher
        fields = (
            'teacher_email',
            'teacher_pass',
        )
    def clean(self):
        email=self.cleaned_data['teacher_email']
        password=self.cleaned_data['teacher_pass']
        res=Teacher.objects.filter(teacher_email=email)
        if res.count()!=1:
            raise forms.ValidationError('Teacher is not registered yet?')
        tr=Teacher.objects.get(teacher_email__exact=email)
        pas=tr.teacher_pass
        if not pbkdf2_sha256.verify(password,pas):
            raise forms.ValidationError("INCORRECT PASSWORD")
        return self.cleaned_data
