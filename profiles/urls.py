from django.urls import path, reverse_lazy
from . import views


app_name = "profiles"   


urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("<int:pk>/update/",views.ProfileUpdateView.as_view(success_url = reverse_lazy('home:home')), name="update"),
    #path("profiles_test/", views.profiles_test, name="profiles_test"),
]
