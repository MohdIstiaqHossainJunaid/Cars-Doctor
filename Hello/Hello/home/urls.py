from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("location",views.location, name='location'),
    path("mecha",views.mecha, name='mecha'),
    path("career",views.career, name='career'),
    path("modeling",views.modeling,name='modeling')

]