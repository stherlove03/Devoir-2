from django.shortcuts import render
#from django.http import HttpResponse
from ecole.models import Etudiants

# Create your views here.
def index(request):
    ecoles = Etudiants.objects.all()
    return render(request, 'index.html', {'ecoles': ecoles})  

