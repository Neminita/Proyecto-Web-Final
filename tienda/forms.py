from typing import Any
from django import forms
from .models import Vinilo
from django.contrib.auth.forms import UserCreationForm
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ViniloForm(forms.ModelForm):

    portada = forms.ImageField(required=True, validators=[MaxSizeFileValidator(max_file_size=10)])

    def clean_titulo(self):
        nombre = self.cleaned_data["nombre"]
        existente = Vinilo.objects.filter(nombre=nombre).exists()

        if existente:
            raise ValidationError("Nombre ya existente de vinilo")
        
        return nombre

    class Meta:
        model = Vinilo
        fields = "__all__"


class CustomUserCreationForm(UserCreationForm):
    pass