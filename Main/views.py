# En Main/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from .forms import CustomUserCreationForm


# ==============================INDEX==============================================
def index(request):
    return render(request, 'Main/index.html')



# ==========================ABOUT ME=================================================
def about_me(request):
    return render(request, 'Main/about_me.html')


# =====================REGISTRO=====================================================
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main:login')  # Cambia 'Main:login' por la URL correspondiente a tu vista de login
    else:
        form = CustomUserCreationForm()

    return render(request, 'Main/register.html', {'form': form})
