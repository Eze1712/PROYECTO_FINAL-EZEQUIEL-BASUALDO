from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese un nombre de usuario único'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese una contraseña segura'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
