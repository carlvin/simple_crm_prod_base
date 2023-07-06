from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.forms import AgentModelForm
from client_relationship_manager.models import Agent


# Create your views here.
class AgentListView(LoginRequiredMixin,generic.ListView):
    template_name = "agent_list.html"
    context_object_name = "agents"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        return Agent.objects.all()
    
class AgentCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = "agent_create.html"
    form_class = AgentModelForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        user = self.request.user
        agent = form.save(commit=False)
        agent.organisation = user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
    
    def get_success_url(self) -> str:
        messages.success(self.request,"Agent Created")
        return reverse_lazy('agents:agent')
    
class AgentDetailView(LoginRequiredMixin,generic.DetailView):
    template_name ="agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = Agent.objects.all()
        return queryset
    
class AgentUpdateView(LoginRequiredMixin,generic.CreateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm  
    
    def get_success_url(self) -> str:
        messages.success(self.request,"Agent Updated")
        return reverse_lazy('agents:agent')