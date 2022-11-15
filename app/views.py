from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import Message
import requests
import json

def index_view(request):
    return render(request, 'index.html')

def saveMessage_view(request):
    objet = request.POST.get('objet')
    message = request.POST.get('message')

    Message.objects.create(subject = objet, message = message)


    url = "http://127.0.0.1:8001/api/message/"
    data = {'email': 'azerty@gmailcom', 'message': message}
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return redirect('/')