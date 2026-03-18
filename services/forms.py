from django import forms
from .models import ServiceRecord

class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['vehicle_name', 'service_type', 'date', 'notes', 'next_service_date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'next_service_date': forms.DateInput(attrs={'type': 'date'}),
        }