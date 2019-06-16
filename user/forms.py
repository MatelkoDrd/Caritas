from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User


class UserProfileForm(ModelForm):

    first_name = forms.CharField(label='Imięeee', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ChangePasswordForm(Form):

    password = forms.CharField(label='Stare hasło', widget=forms.PasswordInput(attrs={'placeholder': 'Poprzednie hasło'}))
    new_password = forms.CharField(label='Nowe hasło', widget=forms.PasswordInput(attrs={'placeholder': 'Nowe hasło'}))
    re_checked = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput(attrs={'placeholder': 'Potwierdź hasło'}))