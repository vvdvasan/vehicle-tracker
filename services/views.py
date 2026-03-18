from django.shortcuts import render, redirect
from .models import ServiceRecord
from .forms import ServiceForm

def home(request):
    records = ServiceRecord.objects.all().order_by('-date')
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'services/home.html', {'records': records, 'form': form})