from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..decorators import athlete_required
from ..forms import AthleteSignUpForm
from ..models import Session, User, Athlete


class AthleteSignUpView(CreateView):
    model = Athlete
    form_class = AthleteSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'athlete'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('coach:athlete_list')


@method_decorator([login_required, athlete_required], name='dispatch')
class SessionListView(ListView):
    model = Session
    ordering = ('date', )
    context_object_name = 'sessions'
    template_name = 'coach/athletes/session_list.html'

    def get_queryset(self):
        athlete = self.request.user.athlete
        athlete_sessions = athlete.sessions.values_list('pk', flat=True)
        queryset = Session.objects.filter(session__in=athlete_sessions) \
            .annotate(sessions_count=Count('sessions')) \
            .filter(sessions_count__gt=0)
        return queryset        