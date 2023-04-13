from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import DatabaseInputForm

# Create your views here.


def homepage(request):
    return render(request, "ABC_Media/home.html")


def login(request):
    form = DatabaseInputForm
    return render(request, "ABC_Media/login.html", context={'form': form})

