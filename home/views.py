from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
# Create your views here.


from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib import messages
from django.views.generic import TemplateView, View

# Create your views here.
#Extra pieces to account for different configurations

class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'index.html', context)

def home(requests):
    return render(requests, 'index.html')

class LoginView(TemplateView):

    template_name = 'registration/login.html'

class AboutView(TemplateView):

    template_name = 'about.html'

class FaqView(TemplateView):

    template_name = 'faq.html'

class ContactView(TemplateView):
 
    template_name = 'contact.html' 
     

