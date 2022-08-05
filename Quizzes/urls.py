from django.urls import path
from . import views 
import Quizzes


app_name='Quizzes'
urlpatterns = [
   path('', views.home,name='home'),
   path('addQuestion/', views.addQuestion,name='addQuestion'),
   path('stuquizhome', views.stuquiz,name='stuquiz'),
   
   
   
   ]