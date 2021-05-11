from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('worker', views.worker, name='worker'),
    path('', views.index, name='index'),
]
