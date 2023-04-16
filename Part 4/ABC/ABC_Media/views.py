from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DatabaseInputForm
from .forms import SearchForm
from django.db import connection
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def homepage(request):

    if 'username' in request.session:
        current_user = request.session['username']
        param = {'current_user': current_user}
    else:
        return redirect("ABC_Media:login")

    return render(request, "ABC_Media/home.html", param)


def login(request):
    if request.method == "POST":
        form = DatabaseInputForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['data_base_name']
            if user in str(connection.settings_dict['NAME']):

                request.session['username'] = user
                messages.info(request, "You logged in!")
                return redirect("ABC_Media:main")
        # display error message
    form = DatabaseInputForm()
    return render(request, "ABC_Media/login.html", {'form': form})


def logout(request):
    try:
        del request.session['username']
    except:
        pass

    return HttpResponseRedirect('/login/')


def main(request):
    if 'username' in request.session:
        current_user = request.session['username']
        form = SearchForm(request.POST)
        param = {'current_user': current_user, 'form': form }
        if request.method == "POST":
            if form.is_valid():
                d_id = form.cleaned_data['digital_display']
                return redirect(search_digi_disp(request, d_id))
        else:
            return render(request, "ABC_Media/main.html", param)
    else:
        return redirect("ABC_Media:login")


# need to work this method out - Rippie
def search_digi_disp(request, d_id):
    return HttpResponse("I got the ID")




