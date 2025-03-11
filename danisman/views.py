from django.shortcuts import render
from .models import Danisman , Uygunluk
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    danisman = Danisman.objects.all()
    for psikolog in danisman:
        for uygunluk in psikolog.availabilities.all():
            uygunluk.start_time = timezone.localtime(uygunluk.start_time)  # Yerel saate dönüştür
            uygunluk.end_time = timezone.localtime(uygunluk.end_time)
    context = {
        'danisman': danisman,
    }
    return render(request , 'danismanbilgi/index.html' , context)


def danisman_details(request , danisman_id):
    danisman = get_object_or_404(Danisman , pk = danisman_id)
    context = {'danisman': danisman}
    return render(request , 'danismanbilgi/details.html' , context)


def danisman_randevu(request , danisman_id):
    danisman = get_object_or_404(Danisman , pk = danisman_id)
    context = {
            'danisman' : danisman
        }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        date = request.POST.get('date', '') 
        comment = request.POST['comment']
        
        send_mail(first_name, 
          last_name, 
          phone, 
          settings.EMAIL_HOST_USER,  # 'settings' burada doğru olmalı
          ['aslanmert451998@gmail.com'],
          fail_silently=False)
    return render(request , 'danismanbilgi/danisman_randevu.html' , context)


