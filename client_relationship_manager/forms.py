from django import forms
from .models import Client

class CreateClientModel(forms.ModelForm):
    class Meta:
        model = Client       
        verbose_name = 'client'
        verbose_name_plural = 'clients'