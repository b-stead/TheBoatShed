from django.shortcuts import render, redirect, get_object_or_404
from profiles.forms import TeamCreateForm
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from profiles.models import Team
# Create your views here.

class TeamView(View):
    def get(self, request):
        tm = Team.objects.all()
        ctx = {'team_list': tm}
        return render(request, 'demo/team_list.html', ctx)

class TeamCreate(CreateView):
    model = Team
    template = 'demo/team_create.html'
    fields = '__all__'
    success_url = reverse_lazy('demo:all_teams')

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('demo:all_teams')

class TeamDelete(DeleteView):
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('demo:all_teams')