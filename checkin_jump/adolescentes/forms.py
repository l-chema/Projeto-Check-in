from django import forms
from .models import Adolescente
from django.core.exceptions import ValidationError
from datetime import datetime

class AdolescenteForm(forms.ModelForm):
    class Meta:
        model = Adolescente
        fields = '__all__'

    # não permite que a data de nascimento seja no futuro
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if data_nascimento and data_nascimento > datetime.now().date():
            raise ValidationError("A data de nascimento não pode ser no futuro.")
        return data_nascimento

    # não permite que a data de início seja no futuro
    def clean_data_inicio(self):
        data_inicio = self.cleaned_data.get('data_inicio')
        if data_inicio and data_inicio > datetime.now().date():
            raise ValidationError("A data de início não pode ser no futuro.")
        return data_inicio

