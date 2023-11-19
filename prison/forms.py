from django import forms
from .models import Prisoner


class PrisonerUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Prisoner
        fields = ("__all__",)
