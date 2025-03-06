from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def index(request):
    return render(request , 'pages/index.html')

def about(request):
    return render(request , 'pages/about.html')

def rezervation(request):
    return render(request , 'pages/rezervation.html')

def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['firstname']
        send_mail(name, 
          message, 
          settings.EMAIL_HOST_USER,  # 'settings' burada doğru olmalı
          [email],
          fail_silently=False)
    return render(request , 'pages/contact.html')
