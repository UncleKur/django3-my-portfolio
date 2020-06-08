from django.shortcuts import render
from .models import Ability

def home(request):
    abilities = Ability.objects.all()
    return render(request, 'portfolio/home.html', {
        'abilities': abilities, 
    })