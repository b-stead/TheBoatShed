
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, ListView)

from ..decorators import coach_required
from ..forms import CoachSignUpForm
from ..models import Session, Coach

class CoachSignUpView(CreateView):
    model = Coach
    form_class = CoachSignUpForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'coach'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('coach:coach_list')

@method_decorator([login_required, coach_required], name='dispatch')
class SessionListView(ListView):
    model = Session
    ordering = ('date', )
    context_object_name = 'sessions'
    template_name = 'coach/coaches/session_list.html'

    def get_queryset(self):
        queryset = self.request.user.sessions\
            .select_related('session') \
            .annotate(sessions_count=Count('sessions', distinct=True)) \
            #.annotate(taken_count=Count('taken_quizzes', distinct=True))
        return queryset