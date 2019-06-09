from django import forms
from django.forms import ModelForm
from user.models import User


class LoginForm(forms.Form):
    name = forms.EmailField(label='Email')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):

    name = forms.CharField(label='Imię')
    last_name = forms.CharField(label='Nazwisko')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'
