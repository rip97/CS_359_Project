from django.urls import path
from . import views


app_name = 'ABC_Media'


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
]