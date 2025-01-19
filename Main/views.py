# En Main/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Vista para la página de inicio (index)
def index(request):
    return render(request, 'Main/index.html')

# Vista para registrar un nuevo usuario
def registro(request):
    return render(request, 'Main/registro.html')
