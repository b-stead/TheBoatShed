from django import forms
from .models import Vbo

class VboUploadForm(forms.ModelForm):
    file = forms.FileField(label='Select a VBO file to upload')
    session_date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=['%d/%m/%Y'])

    class Meta:
        model = Vbo
        fields = ['file','session_date', 'crew', 'session']


