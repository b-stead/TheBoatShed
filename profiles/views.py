from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView, View, ListView, DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import CoachSignUpForm, AthleteSignUpForm, UpdateProfileForm, SquadForm
from .models import Coach, Athlete, User, Squad

def profiles_test(request):
    template_name = 'profiles/test.html'
    context = {}
    return render(request, template_name, context)


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
    model = User
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
    model = User
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


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "profiles/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="profiles/password/password_reset.html", context={"password_reset_form":password_reset_form})


class ProfileUpdateView(LoginRequiredMixin, View):
    model = User
    template_name = 'profiles/update.html'
    success_url = reverse_lazy('home:home')
    
    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = UpdateProfileForm(instance=user)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = UpdateProfileForm(request.POST, request.FILES or None, instance=user)

        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template_name, context)
            #redirect(reverse('profile', kwargs={"username": request.user}))

        user = form.save(commit=False)
        user.save()
        form.save_m2m()
        return redirect(self.success_url)

class SquadCreateView(LoginRequiredMixin, CreateView):
    model = Squad
    template_name = 'profiles/squad_create.html'
    success_url = reverse_lazy('profiles:squad_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_coach:
            return redirect(reverse_lazy('profiles:update'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = SquadForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = get_object_or_404(User, id=user_pk)
        form = SquadForm(request.POST, request.FILES or None, instance=user)

        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template_name, context)

        squad = form.save(commit=False)
        squad.owner = self.request.user
        squad.save()
        return redirect(reverse_lazy('profiles:squad_list', kwargs={'pk': user}))


class SquadList(ListView):
    template_name = 'profiles/squad_list.html'

    def get_queryset(self):
         coach = self.request.user
         print(coach)
         print(coach.pk)

        # Get the squads for which the coach is a coach
         squads = Squad.objects.filter(owner_id=coach.pk)
         print(squads)
         return squads

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['squads'] = self.get_queryset()
        return context


class SquadDetail(DetailView):
     model = Squad