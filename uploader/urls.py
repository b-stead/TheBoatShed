from django.urls import path, reverse_lazy
from .views import VboCreateView, VboListView

app_name = 'uploader'
urlpatterns = [
    path('', VboCreateView.as_view(), name='vbo'),
    path('vbo_list/', VboListView.as_view(), name='vbo_list'),
    

]

"""
path('', VboCreateView.as_view(), name='vbo'),
    
    path('vbo_results/<int:pk>/', VboProcess.as_view(), name='vbo_results'),
    path('process/<int:pk>/', vbo_process, name='vbo_process'),
"""