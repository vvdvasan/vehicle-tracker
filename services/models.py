from django.db import models

class ServiceRecord(models.Model):
    vehicle_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True)
    next_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle_name} - {self.service_type}"