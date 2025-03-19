from django import forms
from .models import Adolescente
from django.core.exceptions import ValidationError
from datetime import datetime

class AdolescenteForm(forms.ModelForm):
    class Meta:
        model = Adolescente
        fields = '__all__'

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if data_nascimento and data_nascimento > datetime.now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        return data_nascimento
