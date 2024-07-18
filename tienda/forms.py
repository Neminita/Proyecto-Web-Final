from django import forms
from .models import Vinilo
from django.contrib.auth.forms import UserCreationForm

class ViniloForm(forms.ModelForm):
    class Meta:
        model = Vinilo
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    pass