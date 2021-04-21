from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Message


def indexCha(request):
    return render(request,'indexCha.html')

def room(request, room_name):
    username = request.GET.get('username', 'Anonymous')
    messages = Message.objects.filter(room=room_name)[0:25]

    return render(request, 'room.html', {'room_name': room_name, 'username': username, 'messages': messages})
