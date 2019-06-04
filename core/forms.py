from django import forms


class LoginForm(forms.Form):
    name = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())