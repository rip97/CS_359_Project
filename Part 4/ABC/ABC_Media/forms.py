# @Author: Justyn Rippie
# @Date: 4-12-2023
# @Description: Custom class for forms

from django import forms


# create a custom form for user login via database

class DatabaseInputForm(forms.Form):

    data_base_name = forms.CharField(label="Data Base Name", max_length=100)


class SearchForm(forms.Form):

    digital_display = forms.CharField(label="Digital Display", max_length=20)



