from django.shortcuts import render, redirect
from .forms import CryptoForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = CryptoForm()
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    else:
        form = CryptoForm()
        return redirect('create')
      
    return render(request, 'dashboard.html')


def update(request):
    pass


def delete(request):
    pass


def dashboard(request):
    pass


def home(request):
    return render(request, 'home.html')
