from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher_name=models.CharField(max_length=100)
    teacher_email=models.EmailField()
    teacher_pass=models.CharField(max_length=200,)
    teacher_cpass=models.CharField(max_length=200)
    phone_no=models.IntegerField()
    img=models.ImageField(upload_to="profile")

    def save(self):
        #Opening the uploaded image
        im = Image.open(self.img)
        output = BytesIO()
        #Resize/modify the image
        im = im.resize( (1376, 768), Image.ANTIALIAS )
        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.img = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.img.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(Teacher,self).save()
    def __str__(self):
        return "name : "+self.teacher_name
