from re import X
from django.shortcuts import render,redirect
from Users.models import *
from .forms import *
# Create your views here.
def addQuestion(request):    
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
        form=addQuestionform()

        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('Quizzes:addQuestion')
        context={'form':form,'type':usertype,'questions':QuesModel.objects.all()}
        return render(request,'Quizzes/instquiz.html',context)
    else: 
        return redirect('Quizzes:addQuestion')

def home(request):
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
    if request.method == 'POST':
        
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            
            if   request.POST[q.question]==q.ans:
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
            ,'type':usertype
        }
        return render(request,'Quizzes/result.html',context)
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
            ,'type':usertype
        }
        return render(request,'Quizzes/stuquiz.html',context)
def stuquiz(request):
    return render(request,'Quizzes/stuquizhome.html')