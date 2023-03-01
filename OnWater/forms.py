from django import forms
from .models import VboData

class VboUploadForm(forms.ModelForm):
    class Meta:
        model = VboData
        fields = ['file']