from django import forms
from .models import Client

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client       
        verbose_name = 'client'
        verbose_name_plural = 'clients'

        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            "address": forms.TextInput(attrs={'class': 'form-input'}),
        }


class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client       
        verbose_name = 'client'
        verbose_name_plural = 'clients'

        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            "address": forms.TextInput(attrs={'class': 'form-input'}),
        }