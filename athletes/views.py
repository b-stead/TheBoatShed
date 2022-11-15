from django.shortcuts import render
from django.views.generic import View
from django.views.generic import ListView, CreateView, DetailView
from . import models
from profiles.models import Athlete, Team, Coach
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .decorators import athlete_required, coach_required
from django.urls import reverse_lazy
# Create your views here.

@method_decorator([login_required, coach_required], name='dispatch')
class CoachView(View):

    def get(self, request):
        ath = Athlete.objects.all().count()
        sq = Team.objects.all()
        ctx = {'Athlete_count':ath, 'Squad_list':sq}
        return render(request, "athletes/coach_home.html", ctx )

@method_decorator([login_required, athlete_required], name='dispatch')
class AthleteView(LoginRequiredMixin, ListView):
    def get(self, request):
        sesh = models.Session.objects.all()
        ctx = {'session_list': sesh}
        return render(request, "athletes/session_list.html", ctx)

class SessionCreateView(CreateView):
    model = models.Session
    fields = '__all__'
    template_name = 'session_create.html'
    success_url = reverse_lazy('athletes:session_create')    

class EffortCreateView(CreateView):
    model = models.Effort
    fields = '__all__'
    template_name = 'Effort_create.html'
    success_url = reverse_lazy('athletes:session_create')

