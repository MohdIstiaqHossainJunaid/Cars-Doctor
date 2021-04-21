from django.urls import path

from . import views
from chatx import views




urlpatterns = [
    path("chatx", views.indexCha, name='indexcha'),
    path('<str:room_name>/', views.room, name='room'),
   
      
]
