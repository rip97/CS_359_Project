from django.urls import path
from . import views


app_name = 'ABC_Media'


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("main/", views.main, name="main"),
    path("create/", views.create, name="create"),
    path("logout/", views.logout, name="logout"),
    path("search_digi_disp/", views.search_digi_disp,name="search")
]