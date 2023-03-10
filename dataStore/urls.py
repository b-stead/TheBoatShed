from django.urls import path, reverse_lazy
from .views import vbo_process

app_name = 'dataStore'
urlpatterns = [
    path('vbo_process/<int:pk>/', vbo_process, name='vbo_process'),

]