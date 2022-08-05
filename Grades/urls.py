from django.urls import path
from . import views 
import Grades

app_name='Grades'
urlpatterns = [
   path('stugrades/',views.stugrades,name='stugrades'),
   path('instgrades/',views.instgrades1,name='instgrades'),
   path('addgrades/',views.addgrades,name='addgrades'),




   
   
   
   ]