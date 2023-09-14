from django.contrib import admin
from django.urls import path
from home import views
app_name = "fileapp"
urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='aboutus'),
    path('contactus',views.contactus,name='contactus'),
    path('upcomming',views.upcomming,name='upcomming'),
    path('signup',views.signup,name='signup'),
    path('login',views.handleLogin,name='handleLogin'),
    path('handleLogout',views.handleLogout,name='hangleLogout'),
    path('registration',views.registration,name='registration'),
    path('comp1',views.comp1,name='comp1'),
    path('upload',views.send_files,name="upload"),
    
    
]
