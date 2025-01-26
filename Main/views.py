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
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('Main:index')
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, "Main/editarPerfil.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "usuario": usuario
    })