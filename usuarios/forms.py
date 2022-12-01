from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme el password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "last_name", "first_name", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Correo electronico")
    
    class Meta:
        model = User
        fields = ["first_name","last_name", "email"]
        help_texts = {k:"" for k in fields}

