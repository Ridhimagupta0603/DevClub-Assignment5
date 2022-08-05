from announcements.models import announcement
from .models import Student, Instructor
from Grades.models import *
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def log_in(request):
	if request.user.is_authenticated:
		return redirect('/authenticated/')
	else:
		if request.method=='POST':
			user_name=request.POST['user_name']
			password=request.POST['password']
			role=request.POST['role']
			userTemp=None
			if (role == "instructor"):
				try:
					userTemp=Instructor.objects.get(username=user_name,password=password)
				except Instructor.DoesNotExist:
					userTemp=None
			elif (role == "student"):
				try:
					userTemp=Student.objects.get(username=user_name,password=password)
				except Student.DoesNotExist:
					userTemp=None
			else:
				user = authenticate(username=user_name, password=password)
				if user is not None:					
					if (user.is_staff == False):
						
						return render(request, "Users/login.html")
					else:
						login(request, user)
						return redirect("/admin/")	
			if userTemp is None:
				return render(request, "Users/login.html")
			else:
				login(request, userTemp)
				return redirect("/authenticated/",{'uname':userTemp.username})						
		else:
			return render(request, "Users/login.html")


def authenticated(request):
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
			course=list(Courses.objects.all())
			student=[]
			
			for c in course:
				
				if c.instructor==userTemp:
					for x in c.students.all():
						student.append(x)
					
			
			return render(request,"Users/insthome.html",{'instructor':userTemp,'student':student,'announcement':announcement.objects.all()})
		elif (usertype=="Student"):
			mycourse=[]
			for x in list(grade.objects.all()):
				if x.student==userTemp:
					mycourse.append(x.course)

			return render(request,"Users/stuhome.html",{'student':userTemp,'mycourse':mycourse,'announcement':announcement.objects.all()})
		else :
			return redirect('/logout/')
	else:
		return redirect('/logout/')

def log_out(request):
	logout(request)

	return redirect('/login/')
