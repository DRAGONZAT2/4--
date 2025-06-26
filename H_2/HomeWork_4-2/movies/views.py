from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    movie = Movie.objects.all()
    return render(request, 'index.html', locals())