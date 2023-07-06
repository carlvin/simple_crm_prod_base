
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from client_relationship_manager.views import SignupView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('client_relationship_manager.urls',namespace='crm')),
    path('agents/',include('agents.urls',namespace='agents')),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',SignupView.as_view(),name='signup'),    
]
