from django.urls import path
from . import views 
import Documents

app_name='Documents'
urlpatterns = [
   path('studoc/',views.studoc,name='studoc'),
   path('instdoclist/',views.instdoc,name='instdoclist'),

   path('instdoc/',views.docform,name='instdoc'),



   
   
   
   ]