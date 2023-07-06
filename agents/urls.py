from django.urls import path
from .views import AgentListView,AgentCreateView,AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('',AgentListView.as_view(),name='agent'),
    path('create_agent/',AgentCreateView.as_view(),name='create-agent'),
    path('<int:pk>/detail/',AgentDetailView.as_view(),name='detail-agent'),
    # path('<int:pk>/update/',UpdateClientView.as_view(),name='update-client'),
    # path('<int:pk>/delete/',DeleteClientView.as_view(),name='delete-client'),
    
]