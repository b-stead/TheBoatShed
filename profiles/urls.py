from django.urls import path
from . import views

app_name = "profiles"   


urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("profile_update/", views.update_profile, name="profile_update"),
    path('athlete/create/', views.athlete_create, name='athlete_create'),
]
