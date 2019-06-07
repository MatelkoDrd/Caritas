from django import forms
from django.forms import ModelForm
from user.models import User


class LoginForm(forms.Form):
    name = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
