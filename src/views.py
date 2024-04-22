from django.shortcuts import render
from album.models import Picha



def home(request):
    pic = Picha.objects.all()
    return render(request, 'index.html', {'pic': pic})


def about(request):
    return render(request, 'about.html')

def price(request):
    return render(request, 'pricing.html')
