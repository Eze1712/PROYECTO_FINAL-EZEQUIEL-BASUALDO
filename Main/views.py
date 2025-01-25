# En Main/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.decorators import login_required



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



# ===================== EDITAR USUARIO =========================================
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=usuario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']

            if informacion.get('password1') and informacion['password1'] == informacion['password2']:
                usuario.set_password(informacion['password1'])

            usuario.save()

            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('Main:index')

    else:
        miFormulario = UserEditForm(instance=usuario)

    return render(request, 'Main/editarPerfil.html', {"miFormulario": miFormulario, "usuario": usuario})
