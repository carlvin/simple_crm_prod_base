from django import forms
from .models import Client, Device

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

class FaultyDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        
        fields = '__all__'
        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-input'}),
            'serial':forms.TextInput(attrs={'class':'form-input'}),
            'siteName':forms.TextInput(attrs={'class':'form-input'}),
            'faultDescription':forms.Textarea(attrs={'class':'form-input'}),
            'technician':forms.TextInput(attrs={'class':'form-input'}),
            
        }
