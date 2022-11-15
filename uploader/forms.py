from django import forms
from django.forms import Select
from .models import Csv

from athletes.models import Athlete

class CsvModelForm(forms.ModelForm):
    athlete_name = forms.ChoiceField(choices=[(ath.uid, ath.name) for ath in Athlete.objects.all()])
    class Meta:
        model = Csv
        fields = ('file_name', 'athlete_name' )
        widgets = {
            'athelte_name': Select(attrs={'class': 'select'}),
        }
