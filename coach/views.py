from django.views.generic import View
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from coach.models import Effort, Athlete, Squads, Session
from coach.owner import OwnerCreateView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import request

from django.contrib.auth import login, authenticate
from django.contrib import messages
# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        ath = Athlete.objects.all().count()
        sq = Squads.objects.all()
        ctx = {'Athlete_count':ath, 'Squad_list':sq}
        return render(request, "coach/coach_home.html", ctx )

class SessionCreateView(OwnerCreateView):
    model = Session
    template_name = 'session_create.html'
    success_url = reverse_lazy('coach:sessions')    

class EffortCreateView(OwnerCreateView):
    model = Effort
    template_name = 'Effort_create.html'
    success_url = reverse_lazy('coach:sessions')

"""
class LoginPageView(View):
    template_name = "registration/login.html"
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ' '
        return render(request, self.template_name, context={'form': form, 'message':message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})

"""


