
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationFm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label="Nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Apellido")
    email = forms.EmailField(max_length=100, required=True, label="Correo Electrónico")
    birth_date = forms.DateField(required=True, label="Fecha de Nacimiento", widget=forms.SelectDateWidget(years=range(1900, 2025)))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2']
