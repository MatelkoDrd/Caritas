from django import forms
from django.forms import ModelForm, Form
from user.models import User


class LoginForm(Form):
    name = forms.EmailField(label='Email ')
    password = forms.CharField(label='Hasło z forms.py', widget=forms.PasswordInput())


class RegisterForm(ModelForm):

    first_name = forms.CharField(label='Imie')
    last_name = forms.CharField(label='Nazwisko')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']
