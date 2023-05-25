from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=240)
    phone = models.CharField(max_length=14)
    address = models.CharField(max_length=300)
    email = models.EmailField(max_length=240)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_success_url(self):
        return reverse_lazy("")

    def get_absolute_url(self):
        return reverse_lazy("crm:detail-client", kwargs={"pk": self.pk})
    