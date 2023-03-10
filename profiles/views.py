from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, TemplateView)
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import CoachSignUpForm, AthleteSignUpForm, UpdateProfileForm, AthleteForm
from .models import Coach, Athlete, User


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

@login_required
def update_profile(request):
    context = {}
    user = request.user 
    form = UpdateProfileForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            update_profile = form.save(commit=False)
            update_profile.user = user
            update_profile.save()
            return redirect("home:home")

    context.update({
        "form": form,
        "title": "Update Profile",
    })
    return render(request, "profiles/update.html", context)

def athlete_create(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.is_athlete = True
            athlete.type = User.Role.ATHLETE # set user type to athlete
            athlete.set_password(form.cleaned_data['password'])
            athlete.save()
            return redirect('athletes:athlete_list')
    else:
        form = AthleteForm()
    return render(request, 'profiles/athlete_create.html', {'form': form})