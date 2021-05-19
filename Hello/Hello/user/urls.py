from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
   
     path("", views.signIn, name='signIn'),  
     path("postsignx/", views.postsign,name="postsignx"),
     path("signUp/", views.signup, name="signup"),
     path("logout/", views.logout, name="log"),
     path("postsignup/", views.postsignup,name="postsignup"),
     path("back/", views.back,name="back"),
      


]