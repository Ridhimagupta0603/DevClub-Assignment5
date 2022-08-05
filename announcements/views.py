from django.shortcuts import render
from Users.models import *
from Grades.models import *
from django.shortcuts import render,redirect
from.forms import annform
from .models import *
# Create your views here.

def ann (request):
    
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
        form=annform()
        if(request.method=='POST'):
            form=annform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/authenticated/')
        context={'form':form,'type':usertype,}
        return render(request,'announcements/announce.html',context)
    else: 
        return redirect('/authenticated/')


def receive(request):
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
        announcements=announcement.objects.all()
        return render(request,'announcements/stuann.html',{'announcements':announcements})
    
def viewann(request):
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
        announcements=announcement.objects.all()
        return render(request,'announcements/viewann.html',{'announcements':announcements})
    
