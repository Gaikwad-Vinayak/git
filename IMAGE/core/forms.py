from .models import img
from django import forms

class imgform(forms.ModelForm):
    class Meta:
        model=img
        fields='__all__'
        labels={'photo':''}