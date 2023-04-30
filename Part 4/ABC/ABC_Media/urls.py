from django.urls import path
from . import views


app_name = 'ABC_Media'


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("main/", views.main, name="main"),
    path("logout/", views.logout, name="logout"),
    path("search_digi_disp/", views.search_digi_disp, name='searched'),
    path("view_all_displays/", views.view_all_displays, name='view_all_displays'),    
    path("update_display/<display_id>", views.update_display, name='update_display'),
    path("delete_display/<display_id>", views.delete_display, name='delete_display'),
    path("add_display/", views.add_display, name='add_display'),
    path("view_all_models/", views.view_all_models, name='viewModels'),
    path("view_model_info/<model_number>", views.view_model_info, name='viewModelInfo'),
    path("add_model/", views.add_model, name='add_model'),    
]