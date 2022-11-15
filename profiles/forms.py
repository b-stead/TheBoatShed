from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Team
# Create your forms here.

class CoachSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_coach")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_coach = True
        if commit:
            user.save()
        return user

class AthleteSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "is_athlete")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_athlete = True
        if commit:
            user.save()
        return user


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model  = Team
        fields = '__all__' 