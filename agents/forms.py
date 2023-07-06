from django import forms
from client_relationship_manager.models import Agent


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = Agent
        
        fields = (
            'user',
        )