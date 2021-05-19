"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chatx  import views as chat
from  user import views as user_views

admin.site.site_header = "Car's Doctor"
admin.site.site_title = "Car's Doctor Admin"
admin.site.index_title = "Welcome to Car's Doctor"

urlpatterns = [
    path('', admin.site.urls),
    path('dfdf', include('home.urls')),
    path('c/', include('chatx.urls')),



   
     path("x", user_views.signIn, name='signIn'),  
     path("postsignx/", user_views.postsignx,name="postsignx"),
     path("signUp/", user_views.signup, name="signup"),
     path("logout/", user_views.logout, name="log"),
     path("postsignup/", user_views.postsignup,name="postsignup"),
     path("back/", user_views.back,name="back"),
      





  
]
    



