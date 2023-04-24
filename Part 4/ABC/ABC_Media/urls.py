from django.urls import path
from . import views


app_name = 'ABC_Media'


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("main/", views.main, name="main"),
    path("logout/", views.logout, name="logout"),
    path("search_digi_disp/", views.search_digi_disp,name="search"),
    path("viewalldisplays/", views.view_all_displays, name='view'),
    path("update_display/", views.update_display, name='update'),
    path("delete_display/", views.delete_display, name='delete')
]