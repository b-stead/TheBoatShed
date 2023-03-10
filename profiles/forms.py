from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Coach
# Create your forms here.

class CoachSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Coach
        fields = ("email",'user_name',"password1", "password2", "is_coach")

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
        fields = ("email",'user_name', "password1", "password2", "is_athlete")

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.is_athlete = True
            if commit:
                user.save()
            return user

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "bio", "profile_pic")


class AthleteForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("email",'user_name', "first_name", "last_name", "password", "is_athlete")
        widgets = {
            'password': forms.PasswordInput(),
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.is_athlete = True
            if commit:
                user.save()
            return user