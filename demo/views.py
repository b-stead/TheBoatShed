from django.shortcuts import render, redirect, get_object_or_404
from profiles.forms import TeamCreateForm
from django.views.generic import View, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import TeamDemo, CoachDemo, AthleteDemo
from .forms import AthleteDemoForm, CoachDemoForm
# Create your views here.

class TeamDemoView(View):
    def get(self, request):
        tm = TeamDemo.objects.all()
        ctx = {'team_list': tm}
        return render(request, 'demo/team_list.html', ctx)

class TeamDemoCreate(CreateView):
    model = TeamDemo
    template = 'demo/team_create.html'
    fields = '__all__'
    success_url = reverse_lazy('demo:team_all')

class TeamUpdate(UpdateView):
    model = TeamDemo
    fields = '__all__'
    success_url = reverse_lazy('demo:team_all')

class TeamDelete(DeleteView):
    model = TeamDemo
    fields = '__all__'
    success_url = reverse_lazy('demo:team_all')


###Atheltes###
class AthleteDemoView(View):
    def get(self, request):
        am = AthleteDemo.objects.all()
        ctx = {'athlete_list': am}
        return render(request, 'demo/athlete_list.html', ctx)

class AthleteDemoCreate(CreateView):
    model = AthleteDemo
    template = 'demo/Athlete_create.html'
    fields = '__all__'
    success_url = reverse_lazy('demo:all_athletes')
    
    def get(self, request):
        form = AthleteDemoForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = AthleteDemoForm(request.POST)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template, ctx)
        athlete = form.save()
        return redirect(self.success_url)


class AthleteDemoUpdate(UpdateView):
    model = AthleteDemo
    fields = '__all__'
    success_url = reverse_lazy('demo:all_athletes')

class AthleteDemoDelete(DeleteView):
    model = AthleteDemo
    fields = '__all__'
    success_url = reverse_lazy('demo:all_athletes')

class AthleteDemoDetailView(DetailView):
    model = AthleteDemo
    template_name = "demo/Athlete_detail.html"
    def get (self, request, pk):
        x = AthleteDemo.objects.get(id=pk)
        context = {'athlete': x}
        return render(request, self.template_name, context)



###Coaches#####
class CoachDemoView(View):
    def get(self, request):
        cm = CoachDemo.objects.all()
        ctx = {'coach_list': cm}
        return render(request, 'demo/coach_list.html', ctx)

class CoachDemoCreate(CreateView):
    model = AthleteDemo
    template = 'demo/coach_create.html'
    fields = '__all__'
    success_url = reverse_lazy('demo:all_coaches')
    def get(self, request):
        form = CoachDemoForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = CoachDemoForm(request.POST)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request, self.template, ctx)
        coach = form.save()
        return redirect(self.success_url)

class CoachDemoUpdate(UpdateView):
    model = CoachDemo
    fields = '__all__'
    success_url = reverse_lazy('demo:all_coaches')

class CoachDemoDelete(DeleteView):
    model = CoachDemo
    fields = '__all__'
    success_url = reverse_lazy('ddemo:all_coaches')