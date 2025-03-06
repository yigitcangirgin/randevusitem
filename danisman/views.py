from django.shortcuts import render
from .models import Danisman
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    danisman = Danisman.objects.all()
    context = {
        'danisman': danisman
    }
    return render(request , 'danismanbilgi/index.html' , context)


def danisman_details(request , danisman_id):
    danisman = get_object_or_404(Danisman , pk = danisman_id)
    context = {'danisman': danisman}
    return render(request , 'danismanbilgi/details.html' , context)

