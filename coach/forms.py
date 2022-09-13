from dataclasses import fields
from django import forms
from .models import Coach, Athlete
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.forms.utils import ValidationError


# form for vbo upload
class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'dob', 'gender', 'discipline', 'classification', 'club']

class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['name', 'email', 'user'] 

"""
class SquadForm(forms.ModelForm):
    class Meta:
        model = Squad
        fields = ['name', 'athlete', 'coach'] 
		"""


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	name = forms.CharField(max_length=30)

	class Meta:
		model = Coach
		
		fields = ("name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user