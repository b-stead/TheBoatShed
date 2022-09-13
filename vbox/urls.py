from django.urls import path, reverse_lazy
from .views import vbox_info
app_name ='vbox'
urlpatterns =[

    path('vbox', vbox_info, name='all'),

]