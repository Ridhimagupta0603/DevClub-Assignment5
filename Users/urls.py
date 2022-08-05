from django.urls import path
from Users import views 


urlpatterns = [
   path('',views.log_in,name='login'),
   path('login/',views.log_in,name='login'),
   path('authenticated/',views.authenticated,name='authenticated'),
   path('logout/',views.log_out,name='logout'),



   
   
   
   ]