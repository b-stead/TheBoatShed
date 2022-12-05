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

class ShedView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, 'index.html', context)

def home(request):
    if request.user.is_authenticated:
        if request.user.is_coach:
            return redirect('athletes:coach')
        else:
            return render(request, 'index.html')
    return render(request, 'index.html')

class LoginView(TemplateView):

    template_name = 'registration/login.html'

class AboutView(TemplateView):

    template_name = 'about.html'

class FaqView(TemplateView):

    template_name = 'faq.html'

class ContactView(TemplateView):
 
    template_name = 'contact.html' 
     

def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'500.html', data)
