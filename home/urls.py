from django.urls import path

from .views import AboutView, ShedView, FaqView, ContactView, home
from django.contrib.auth import views as auth_views
app_name = 'home'

urlpatterns = [
    path('', ShedView.as_view(), name='boat_shed'),
    path('home/', home, name='home'), 
    path('about/', AboutView.as_view(), name='about'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('contact/', ContactView.as_view(), name='contact'),

]
