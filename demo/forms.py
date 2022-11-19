
from django import forms
from .models import TeamDemo, AthleteDemo, CoachDemo
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import User
from .widgets import FengyuanChenDatePickerInput


class DateInput(forms.DateInput):
    input_type = 'date'

class TeamDemoCreateForm(forms.ModelForm):
    class Meta:
        model = TeamDemo
        fields = '__all__'

class CoachDemoForm(forms.ModelForm):
    class Meta:
        model = CoachDemo
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput()
        }

class AthleteDemoForm(forms.ModelForm):
    class Meta:
        model = AthleteDemo
        fields = '__all__'
        widgets = {
            'date_of_birth': DateInput()
        }
        

        