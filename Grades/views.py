from django.shortcuts import render,redirect
from Users.models import Student,Instructor
from Grades.models import Courses,grade
from .form import *
# Create your views here.
def stugrades(request):
    usertype="NULL"
    if request.user.is_authenticated:
        try:
            userTemp=Instructor.objects.get(username=request.user.username,password=request.user.password)
            usertype="Instructor"
        except Instructor.DoesNotExist:
            userTemp=None

    if (userTemp==None):
        try:
            userTemp=Student.objects.get(username=request.user.username,password=request.user.password)
            usertype="Student"
        except Student.DoesNotExist:
            userTemp=None

    if (usertype=="Student"):
        courses=userTemp.courses_set.all()
        ga=list(userTemp.grade_set.all())
        y,z=0,0
        for x in ga:
            y+=(x.course.credit)*(x.course_grade)
            z+=(x.course.credit)
        a=y/z


        
        return render(request,'Grades/stugrades.html',{'student':userTemp,'courses':courses,'ga':ga,'a':a})

def instgrades(request):
    usertype="NULL"
    if request.user.is_authenticated:
        try:
            userTemp=Instructor.objects.get(username=request.user.username,password=request.user.password)
            usertype="Instructor"
        except Instructor.DoesNotExist:
            userTemp=None

    if (userTemp==None):
        try:
            userTemp=Student.objects.get(username=request.user.username,password=request.user.password)
            usertype="Student"
        except Student.DoesNotExist:
            userTemp=None

    if (usertype=="Instructor"):
        stu=Student.objects.all()
        grades=grade.objects.all()
    return render(request,'Grades/instgrades.html',{'stu':stu,'grades':grades})
def instgrades1(request):
    if request.method=="POST":
        if request.user.is_authenticated:
            try:
                userTemp=Instructor.objects.get(username=request.user.username,password=request.user.password)
            except Instructor.DoesNotExist:
                return redirect('/logout/')

            course=Courses.objects.get(instructor=userTemp)
            gr=list(grade.objects.filter(course=course))
            



            for x in gr:
                course_grade=request.POST['course_grade']
                x.course_grade=course_grade
                x.save()
                
                
            return redirect('/grades/instgrades/')
        else:
            return redirect('/logout/')


    else:
        if request.user.is_authenticated:
            try:
                userTemp=Instructor.objects.get(username=request.user.username,password=request.user.password)
            except Instructor.DoesNotExist:
                return redirect('/logout/')
            
            stu=Student.objects.all()
            grades=grade.objects.all()
            course=Courses.objects.get(instructor=userTemp)
            gr=list(grade.objects.filter(course=course))
            """for std in Student.objects.all():
                for c in std.courses_set.all():
                    try:
                        r=grade.objects.get(student=std,course=c)
                    except r.DoesNotExist:
                        r=grade.objects.get(student=std,course=c)
                        r.save()"""
            
            for std in Student.objects.all():
                
                    try:
                        r=grade.objects.get(student=std,course=1)
                    except r.DoesNotExist:
                        r=grade(student=std)
                        r.save()
            
        
        
        return render(request,"Grades/instgrades.html",{'stu':stu,'grades':grades,'course':course,'gr':gr})
    
def addgrades(request):
    usertype="NULL"
    if request.user.is_authenticated:
        try:
            userTemp=Instructor.objects.get(username=request.user.username,password=request.user.password)
            usertype="Instructor"
        except Instructor.DoesNotExist:
            userTemp=None

    if (userTemp==None):
        try:
            userTemp=Student.objects.get(username=request.user.username,password=request.user.password)
            usertype="Student"
        except Student.DoesNotExist:
            userTemp=None
    if (usertype=="Instructor"):
        form=addgradesform()
        if(request.method=='POST'):
            form=addgradesform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('Grades:addgrades')
        context={'form':form,'type':usertype,'g':grade.objects.all()}
        return render(request,'Grades/addgrades.html',context)
    else: 
        return redirect('Grades:addgrades')