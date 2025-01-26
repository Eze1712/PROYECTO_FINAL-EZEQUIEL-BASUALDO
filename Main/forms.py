from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

#Form para crear usuario en register
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese un nombre de usuario único'}))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su apellido'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese una contraseña segura'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña'}))
    avatar = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'accept': 'image/*'}))  # Campo de avatar

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'avatar']  # Agregar avatar a los campos

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Crear el perfil asociado al usuario
            profile = Profile.objects.create(user=user)
            if self.cleaned_data.get('avatar'):
                profile.avatar = self.cleaned_data['avatar']
                profile.save()  # Guardar el perfil con el avatar
        return user

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


#Form para modificar usuario

class UserEditForm(UserChangeForm):
    password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'last_name', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2