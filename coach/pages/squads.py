from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from ..models import Squads
from ..forms import SquadCreateForm
from django.views.generic import CreateView


class SignUpView(TemplateView):
    template_name = 'coach/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_coach:
            return redirect('coach:athlete_list')
        else:
            return redirect('athletes:session_list')
    return render(request, 'coach/coach_home.html')


class SquadCreateView(CreateView):
    model = Squads
    form_class = SquadCreateForm
    template_name = 'squad-create.html'
    success_url = reverse_lazy('coach:home')    