from sched import scheduler
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import DatabaseInputForm
from .forms import SearchForm
from django.db import connection
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Digitaldisplay, Model
from .forms import DigitalDisplayForm, DigitalDisplayFormUpdate, ModelInfoForm, ModelCreateForm
from django.contrib import messages
import re

#Pagination
from django.core.paginator import Paginator

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
        # form = SearchForm(request.POST)
        param = {'current_user': current_user}
        #if request.method == "POST":
            #if form.is_valid():
               # d_id = form.cleaned_data['digital_display']
               # return redirect(search_digi_disp(request, d_id))

        return render(request, "ABC_Media/main.html", param)
    else:
        return redirect("ABC_Media:login")


# need to work this method out - Rippie
# def search_digi_disp(request):
#     if 'username' in request.session:
#         current_user = request.session['username']
#         searched = request.POST['searched']
#         digital_display = Digitaldisplay.objects.get(pk=searched)
#         digital_display_search_results = []
#         for display in Digitaldisplay.objects.all():
#             if searched in display.serialno:
#                 digital_display_search_results.append(digital_display)
#         param = {'current_user': current_user, 'searched': searched,
#                  'digital_display': digital_display}
#         return render(request, "ABC_Media/searched.html", param)

#     else:
#         return redirect("ABC_Media:login")

def search_digi_disp(request):
    if 'username' in request.session:
        current_user = request.session['username']
        searched = request.POST['searched']
        # digital_display = Digitaldisplay.objects.get(pk=searched)
        digital_display_search_results = []
        for display in Digitaldisplay.objects.all():
            if searched in display.serialno:
                digital_display_search_results.append(display)
        # param = {'current_user': current_user, 'searched': searched,
        #          'digital_displays': digital_display_search_results}
        p = Paginator(digital_display_search_results, 7)
        page = request.GET.get('page')
        displays = p.get_page(page)

        context = {
            'displays': displays,
            'current_user': current_user,
            'searched' : searched
            }
        return render(request, "ABC_Media/viewdisplays.html", context)

    else:
        return redirect("ABC_Media:login")




def view_all_displays(request):
    #With Order by warning is suppressed, depends on number of objects in the database.
    #p = Paginator(Digitaldisplay.objects.all().order_by("serialno"), 20) 
    if 'username' in request.session:
        current_user = request.session['username']
    p = Paginator(Digitaldisplay.objects.all(), 7)
    page = request.GET.get('page')
    displays = p.get_page(page)

    context = {
        'displays': displays,
        'current_user': current_user,
        'searched':''
        }

    return render(request, 'ABC_Media/viewdisplays.html', context)

def add_display(request):
    models = Model.objects.all()
    submitted = False


    if request.method == "POST":
        form = DigitalDisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_all_displays',request)
    else: 
        form = DigitalDisplayForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'models': models,
        'current_user' : request.session['username']
        }

    return render(request, 'ABC_Media/adddisplay.html', context)

def update_display(request, display_id):
    digital_display = Digitaldisplay.objects.get(pk=display_id)
    form = DigitalDisplayFormUpdate(request.POST or None, instance=digital_display)

    if form.is_valid():
        form.save()
        return redirect('/view_all_displays',request)

    context = {
        'digital_display': digital_display,
        'form': form,
        'current_user' : request.session['username']
        }

    return render(request, 'ABC_Media/updatedisplay.html', context)

def delete_display(request, display_id):    
    digital_display = Digitaldisplay.objects.get(pk=display_id) #Get Display with display_id
    modelNo = digital_display.modelno #Pull ModelNo from the Display Object
    models = Model.objects.get(pk=modelNo) #Pull associated model using Display Model No
    digital_display.delete() #Delete Display

    #Add Logic to Check for other Displays Sharing the Same Model No. If none, delete from Model Table
    modelCount = Digitaldisplay.objects.filter(modelno=modelNo).count()
    if (modelCount > 1): 
        return redirect('/view_all_displays',request)
    else:
        models.delete()
        return redirect('/view_all_displays',request)


def view_all_models(request):
    models = Model.objects.all()

    context = {
        'models': models,
        'current_user' : request.session['username']
        }

    return render(request, 'ABC_Media/viewmodels.html', context)

def view_model_info(request, model_number):
    models = Model.objects.get(pk=model_number)
    form = ModelInfoForm(request.POST or None, instance=models)

    context = {
        'models': models,
        'form': form,
        'current_user' : request.session['username']
        }

    return render(request, 'ABC_Media/modelinfo.html', context)

def add_model(request):
    models = Model.objects.all()
    submitted = False

    if request.method == "POST":
        form = ModelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/add_display')
    else: 
        form = ModelCreateForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'models': models,
        'current_user' : request.session['username']
        }

    return render(request, 'ABC_Media/addmodel.html', context)
