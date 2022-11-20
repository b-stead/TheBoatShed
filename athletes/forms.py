from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Athlete, Session, Effort
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User

class SessionCreateForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'


class AthleteSignUpForm(UserCreationForm):
    sessions = forms.ModelMultipleChoiceField(
        queryset=Session.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_athlete = True
        user.save()
        athlete = Athlete.objects.create(user=user)
        athlete.session.add(*self.cleaned_data.get('sessions'))
        return user

class CoachSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_coach = True
        if commit:
            user.save()
        return user

class EffortCreateForm(forms.ModelForm):
    class Meta:
        model = Effort
        fields = '__all__'


"""
class AthleteCreateForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'
"""        
