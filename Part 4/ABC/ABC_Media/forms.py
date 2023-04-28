# @Author: Justyn Rippie
# @Date: 4-12-2023
# @Description: Custom class for forms

from turtle import width
from django import forms
from django.forms import ModelForm
from .models import Model, Digitaldisplay

# create a custom form for user login via database

class DatabaseInputForm(forms.Form):

    data_base_name = forms.CharField(label="Data Base Name", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))


class SearchForm(forms.Form):

    digital_display = forms.CharField(label="Digital Display", max_length=20, widget=forms.TextInput(attrs={"class": "form-control"}))


#Create Digtal Display
class DigitalDisplayForm(ModelForm):
    class Meta:
        model = Digitaldisplay
        fields = ('serialno', 'schedulersystem', 'modelno')

        DISPLAY_SYSTEMS = [
            ('Smart', 'Smart'),
            ('Random', 'Random'),
            ('Virtue', 'Virtue'),
        ]

        labels = {
            'serialno': 'Serial Number:',
            'schedulersystem': 'Scheduler System',
            'modelno': 'Model Number',
            }

        widgets = {
            'serialno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Serial Number'}),
            'schedulersystem': forms.Select(choices=DISPLAY_SYSTEMS, attrs={"class": " form-select "}),
            'modelno': forms.Select( attrs={"class": " form-select "}),
            }


#Update Form for Digital Displays PK Field is disabled
class DigitalDisplayFormUpdate(ModelForm):
    class Meta:
        model = Digitaldisplay
        fields = ('serialno', 'schedulersystem', 'modelno')

        DISPLAY_SYSTEMS = [
            ('Smart', 'Smart'),
            ('Random', 'Random'),
            ('Virtue', 'Virtue'),
        ]

        labels = {
            'serialno': 'Serial Number:',
            'schedulersystem': 'Scheduler System',
            'modelno': 'Model Number',
            }

        widgets = {
            'serialno': forms.TextInput(attrs={'disabled': 'true', "class": " form-control"}),
            'schedulersystem': forms.Select(choices=DISPLAY_SYSTEMS, attrs={"class": " form-select "}),
            }

#Model Form Create
class ModelCreateForm(ModelForm):
    class Meta:
        model = Model
        fields= ('modelno', 'width', 'height', 'weight','depth','screensize')        


        labels = {
            'modelno': 'Model Number', 
            'width': 'Width', 
            'height': 'Height', 
            'weight': 'Weigth',
            'depth': 'Depth',
            'screensize': 'Screen Size',
            }

        widgets = {
            'modelno': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Model Number', 'style': 'width: 20%'}), 
            'width': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Width', 'style': 'width: 20%'}), 
            'height': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Height', 'style': 'width: 20%'}), 
            'weight': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Weight', 'style': 'width: 20%'}), 
            'depth': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Depth', 'style': 'width: 20%'}), 
            'screensize': forms.TextInput(attrs={'class': ' form-control', 'placeholder': 'Screen Size', 'style': 'width: 20%'}), 
            }

#Model Form View
class ModelInfoForm(ModelForm):
    class Meta:
        model = Model
        fields= ('modelno', 'width', 'height', 'weight','depth','screensize')        


        labels = {
            'modelno': 'Model Number', 
            'width': 'Width', 
            'height': 'Height', 
            'weight': 'Weigth',
            'depth': 'Depth',
            'screensize': 'Screen Size',
            }

        widgets = {
            'modelno': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}), 
            'width': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}), 
            'height': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}), 
            'weight': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}),
            'depth': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}),
            'screensize': forms.TextInput(attrs={'disabled': 'true', "class":"form-control"}),
            }