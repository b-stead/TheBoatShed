from django.urls import path, reverse_lazy
from . import views


app_name = "profiles"   


urlpatterns = [
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("<int:pk>/update/",views.ProfileUpdateView.as_view(success_url = reverse_lazy('home:home')), name="update"),
    path("squad/create/<int:pk>/", views.SquadCreateView.as_view(success_url = reverse_lazy('profiles:squad_list')), name = 'squad_create'),
    path("<int:pk>/squads/", views.SquadList.as_view(), name = 'squad_list'),
    path("squad/<int:pk>/", views.SquadDetail.as_view(), name = 'squad_detail'),
    #path("profiles_test/", views.profiles_test, name="profiles_test"),
]
