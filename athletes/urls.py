from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from athletes.dash_apps.finished_apps import metrics_web2
app_name = "athletes"

urlpatterns = [
    path('', views.CoachView.as_view(), name='coach'),
    path('session/create', views.SessionCreateView.as_view(), name='session_create'),
    path('effort/create', views.EffortCreateView.as_view(), name='effort_create'),
    path('venue/create', views.VenueCreateView.as_view(), name='venue_create'),

    path('athlete-list/', views.AthleteListView.as_view(), name='athlete_list'),
    
    path('athletes/', include(([
        path('', views.AthleteView.as_view(), name='athlete'),
        
    ]))),

]