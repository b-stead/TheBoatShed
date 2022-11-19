from django.urls import path, include
from .views import TeamDemoCreate, TeamDemoView, TeamUpdate, TeamDelete
from .views import CoachDemoView, CoachDemoCreate, CoachDemoDelete, CoachDemoUpdate
from.views import AthleteDemoCreate, AthleteDemoDelete, AthleteDemoUpdate, AthleteDemoView, AthleteDemoDetailView
from django.views.generic import TemplateView
from demo.dash_apps.finished_apps import BenchDash

app_name = "demo"

urlpatterns = [
    path('team/', TeamDemoView.as_view(), name='team_all'),
    path('', TemplateView.as_view(template_name='demo_home.html'), name='demo_home'),
    path('team/create', TeamDemoCreate.as_view(), name='team_create'),
    path('team/<int:pk>/update/', TeamUpdate.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', TeamDelete.as_view(), name='team_delete'),

    path('athlete/', AthleteDemoView.as_view(), name='all_athletes'),
    path('athlete/create', AthleteDemoCreate.as_view(), name='athlete_create'),
    path('athlete/<int:pk>', AthleteDemoDetailView.as_view(), name='athlete_detail'),
    path('athlete/<int:pk>/update/', AthleteDemoUpdate.as_view(), name='athlete_update'),
    path('athlete/<int:pk>/delete/', AthleteDemoDelete.as_view(), name='athlete_delete'),

    path('coach/', CoachDemoView.as_view(), name='all_coaches'),
    path('coach/create', CoachDemoCreate.as_view(), name='coach_create'),
    path('coach/<int:pk>/update/', CoachDemoUpdate.as_view(), name='coach_update'),
    path('coach/<int:pk>/delete/', CoachDemoDelete.as_view(), name='coach_delete'),


]
