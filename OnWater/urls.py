from django.urls import path
from .views import OnWater_home, OnWater_vbo
from . import views
from django.contrib.auth import views as auth_views
from OnWater.dash_apps.finished_apps import vbo_load

app_name = 'OnWater'
urlpatterns = [
    path('water', views.OnWater_home, name='Water'),
    path('vbo', views.OnWater_vbo, name='vbo'),

    
]