from django.urls import path, include
from .pages import athletes, coaches, squads
from . import views


app_name = "coach"

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('session/create', views.SessionCreateView.as_view(), name='session_create'),
    path('effort/create', views.EffortCreateView.as_view(), name='effort_create'),

    path('athletes/', include(([
        path('', athletes.SessionListView.as_view(), name='athlete_list'),


    ]))),

    path('coaches/', include(([
        path('', coaches.SessionListView.as_view(), name='coach_list'),


    ]))),
    
    path('squads/', include(([
        path('', squads.SquadCreateView.as_view(), name='squad_create'),
        path('', squads.SignUpView.as_view(), name='signup'),


    ]))),

]
