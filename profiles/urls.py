from django.urls import path
from . import views

app_name = "profiles"   


urlpatterns = [
    path("password_reset", views.password_reset_request, name="password_reset"),
]
