from django import forms

from .models import DataRecording


class DataRecordingForm(forms.ModelForm):
    class Meta:
        model = DataRecording
        fields = ['file']
