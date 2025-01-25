from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#Form para crear usuario en register
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