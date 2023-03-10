from dataclasses import fields
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from .models import Athlete, Session, Effort, BoatType, BOATTYPE, Venue
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User

class SessionCreateForm(forms.ModelForm):
    boat = forms.ModelChoiceField(queryset=BoatType.objects.all(), 
                                  empty_label=None, label="Boat Type", 
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Session
        exclude = ['uid', 'created_at']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SessionCreateForm, self).__init__(*args, **kwargs)
        self.fields['boat'].choices = BOATTYPE

    def form_valid(self, form):
        # Check if all required foreign key fields have a value
        if form.instance.athlete is None:
            # Redirect the user to the boat creation form
            return redirect(reverse_lazy('athlete_signup'))
        
        if form.instance.venue is None:
            # Redirect the user to the boat creation form
            return redirect(reverse_lazy('venue_create'))
        
        # Set the athlete before saving the form
        form.instance.athlete = self.request.user.athlete
        
        return super().form_valid(form)
    

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

class VenueCreateForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


"""
class AthleteCreateForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = '__all__'
"""        
