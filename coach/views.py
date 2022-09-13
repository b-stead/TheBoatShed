from asyncio import subprocess
from decimal import BasicContext
from re import template

from coach.models import Athlete, Coach
from coach.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerDetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm
from django.views.generic import TemplateView, CreateView, View

# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("coach:athletes")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="coach/register.html", context={"register_form":form})

class AthleteListView(OwnerListView):
    model = Athlete

class AthleteDetailView(OwnerDetailView):
    model = Athlete
    template_name = "coach/athlete_detail.html"

class AthleteCreateView(OwnerCreateView):
    model = Athlete
    template_name = 'coach/athlete_form.html'
    fields = ['name', 'dob', 'gender', 'discipline', 'classification', 'club', 'status']  
    success_url = reverse_lazy('coach:athletes')

class CoachCreateView(OwnerCreateView):
    model = Coach
    template_name = 'coach/coach_form.html'
    success_url = reverse_lazy('coach:athletes')

"""
class SquadListView(OwnerListView):
    model = Squad

class SquadDetailView(OwnerDetailView):
    model = Squad
    template_name = "coach/squad_detail.html"

class SquadCreateView(OwnerCreateView):
    model = Squad
    template_name = 'coach/squad_form.html'
    fields = ['name', 'athlete', 'coach']  
    success_url = reverse_lazy('coach:squad')
    
    """

def about_us(request):
    return render(request, 'coach/about_us.html')

