from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from OnWater.dash_apps.finished_apps import vbo_load, gps_load

app_name = 'OnWater'
urlpatterns = [
    path('water/', views.OnWater_home, name='water'),
    path('vbo/', views.OnWater_vbo, name='vbo'),

    
]