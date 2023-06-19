from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

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
    

class Device(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    serial=models.CharField(_("Serial No"), max_length=50)
    siteName=models.CharField(_("Site "), max_length=50)
    faultTitle=models.CharField(_("Fault Title"), max_length=50)
    faultDescription=models.TextField(_("Fault Description"))
    technician=models.CharField(_("Technician"), max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name} from: {self.siteName}'
    
    def get_success_url(self):
        return reverse_lazy("")
    
    def get_absolute_url(self):
        return reverse_lazy("crm:detail-returned-device", kwargs={"pk": self.pk})
    