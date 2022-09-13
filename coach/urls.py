from django.urls import path, reverse_lazy
from . import views
from .views import about_us
app_name ='coach'
urlpatterns =[


    path('', views.AthleteListView.as_view(), name='athletes'),
    path('athlete/create', views.AthleteCreateView.as_view(success_url=reverse_lazy('coach:athletes')), name='athlete_create'),
    path('athlete/<int:pk>', views.AthleteDetailView.as_view(), name='athlete_detail'),
    path('create', views.CoachCreateView.as_view(), name='coach_create'),
    #path('squad/create', views.SquadCreateView.as_view(), name='squad_create'),
    #path('squad', views.SquadListView.as_view(), name='squad'),
    #path('squad/<int:pk>', views.SquadDetailView.as_view(), name='squad_detail'),
    path('about_us', about_us, name='about_us'),

    path('register/',  views.register_request, name='register'),

]