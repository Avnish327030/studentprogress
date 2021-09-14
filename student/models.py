
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from home.models import Teacher
from exam.models import Exam
class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    rollno=models.IntegerField()
    std=models.IntegerField()
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    img=models.ImageField()
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    medium=models.CharField(max_length=100)
    school_name=models.CharField(max_length=500)

    def save(self):
        # Opening the uploaded image
        im = Image.open(self.img)
        output = BytesIO()
        # Resize/modify the image
        im = im.resize((500, 420), Image.ANTIALIAS)
        # after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        # change the imagefield value to be the newley modifed image value
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)
        super(Student, self).save()
    def __str__(self):
        return self.fname +" has roll no"+str(self.rollno)+"and study in "+self.school_name


class StudentMarks(models.Model):
    mark_id=models.AutoField(primary_key=True)
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    obtain_mark=models.IntegerField()
    def __str__(self):
        return str(self.student_id)+" score "+str(self.obtain_mark)