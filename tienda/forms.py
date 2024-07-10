from django import forms
from .models import Vinilo

class ViniloForm(forms.ModelForm):
    class Meta:
        model = Vinilo
        fields = "__all__"