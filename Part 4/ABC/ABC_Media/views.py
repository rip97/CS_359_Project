from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login(request):
    template = loader.get_template("ABC_Media/login.html")
    return render(request, "ABC_Media/login.html")
