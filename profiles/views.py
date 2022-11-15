from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, TemplateView)

from .forms import CoachSignUpForm, AthleteSignUpForm
from .models import Coach, Athlete

class SignUpView(TemplateView):
    template_name = 'profiles/signup.html'


    def home(request):
        if request.user.is_authenticated:
            if request.user.is_coach:
                return redirect('home:home')
            else:
                return redirect('home:home')
        return render(request, 'home:home')

class CoachSignUpView(CreateView):
    model = Coach
    form_class = CoachSignUpForm
    template_name = 'profiles/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'coach'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        backend= 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user, backend)
        return redirect('home:home')

class AthleteSignUpView(CreateView):
    model = Athlete
    form_class = AthleteSignUpForm
    template_name = 'profiles/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'athlete'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        backend= 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user, backend)
        return redirect('home:home')