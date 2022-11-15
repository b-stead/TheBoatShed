from django.urls import path, include
from . import views
from .views import TeamCreate, TeamView, TeamUpdate, TeamDelete
from django.views.generic import TemplateView
from demo.dash_apps.finished_apps import BenchDash
app_name = "demo"

urlpatterns = [
    path('team/', TeamView.as_view(), name='team_all'),
    path('', TemplateView.as_view(template_name='demo_home.html'), name='demo_home'),
    path('team/create', views.TeamCreate.as_view(), name='team_create'),
    path('team/<int:pk>/update/', views.TeamUpdate.as_view(), name='team_update'),
    path('team/<int:pk>/delete/', views.TeamDelete.as_view(), name='team_delete'),


]
