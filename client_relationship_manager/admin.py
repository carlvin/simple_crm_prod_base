from django.contrib import admin
from .models import Client, Device

# Register your models her
admin.site.register(Client)
admin.site.register(Device)