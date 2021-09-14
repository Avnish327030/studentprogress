from django.db import models

# Create your models here.
from home.models import Teacher
class Exam(models.Model):
    exam_id=models.AutoField(primary_key=True)
    exam_date=models.DateTimeField()
    std=models.IntegerField()
    subject=models.CharField(max_length=100)
    chapter=models.CharField(max_length=100)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    total_mark=models.IntegerField()


    def __str__(self):
        return "EXAM  OF "+self.subject+" on "+self.chapter+ " held on "+str(self.exam_date.date())+ " TOTAL MARKS "+str(self.total_mark)

