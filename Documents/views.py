from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import Docform
from .models import Doc
from Users.models import Instructor,Student
def docform(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":
            Docu=Doc.objects.all()
            form = Docform(request.POST, request.FILES)
            if form.is_valid():
                entry = form.save(commit=False)
                
                entry.file_name = request.POST['file_name']
                form.save()
            
        else:
            form = Docform()
            Docu=Doc.objects.all()
            
        return render(request, "Documents/instdoc.html",locals())
    

    

def studoc(request):
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
        Docu=Doc.objects.all()


        
        return render(request,'Documents/studoc.html',{'student':userTemp,'doc':Docu})
    if (usertype=="Instructor"):
        Docu=Doc.objects.all()


        
        return render(request,'Documents/instdoc.html',{'instructor':userTemp,'doc':Docu})
    

def instdoc(request):
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
        Docu=Doc.objects.all()


        
        return render(request,'Documents/instdoclist.html',{'instructor':userTemp,'doc':Docu})
    

