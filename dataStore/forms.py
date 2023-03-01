from .models import SessionPeaks
from profiles.models import Athlete, Coach
from django import forms

class SessionPeaksForm(forms.ModelForm):
    athletes = forms.ModelMultipleChoiceField(queryset=Athlete.objects.none(), required=False)
    class Meta:
        model = SessionPeaks
        fields = ['session_type','athletes']

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        self.fields['athletes'].queryset = Athlete.objects.filter(squads__coach=user).distinct()

    def update_session_type(self, session_type):
        session_peaks = self.instance
        session_peaks.session_type = session_type
        session_peaks.save()
        session_peaks.athletes.set(self.cleaned_data['athletes'])
        return session_peaks
    

        