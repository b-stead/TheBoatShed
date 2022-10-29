from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth import login
from django.shortcuts import redirect

