# En Main/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect


# ==============================INDEX==============================================
def index(request):
    return render(request, 'Main/index.html')



# ==========================ABOUT ME=================================================
def about_me(request):
    return render(request, 'Main/about_me.html')


# =====================REGISTRO=====================================================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente. \'Ahora puedes iniciar sesisón.')
            return redirect('Main:login')
    else:
        form = UserCreationForm()
    return render(request, 'Main/register.html', {'form': form})