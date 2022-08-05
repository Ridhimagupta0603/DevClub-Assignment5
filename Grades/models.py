from django.db import models
from Users.models import Instructor,Student
# Create your models here.

class Courses(models.Model):
    course_name = models.CharField(max_length=30)
    credit = models.PositiveSmallIntegerField(default=3)
    
    instructor = models.ForeignKey(Instructor,on_delete=models.PROTECT,null=True)
    students = models.ManyToManyField(Student)
    
    
    
    def __str__(self):
        return self.course_name
class grade(models.Model):
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    course_grade= models.IntegerField(default=0)
    def __str__(self):
        return str(self.student.username+" "+self.course.course_name+" "+str(self.course_grade))
