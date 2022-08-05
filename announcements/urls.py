from django.urls import path
from . import views 
import announcements

app_name='announcements'
urlpatterns = [
   path('send/',views.ann,name='send'),
   path('recieve/',views.receive,name='receive'),
   path('viewann/',views.viewann,name='viewann'),


   




   
   
   
   ]