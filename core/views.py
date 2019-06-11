from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.response import TemplateResponse
from django.views import View
from core.forms import LoginForm
from core.forms import RegisterForm
from user.models import User


class BaseView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return TemplateResponse(request, 'base.html', {})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = request.GET.get('next')
        print(next_page)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user = authenticate(username=name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)

                if user.is_superuser:
                    return HttpResponseRedirect('/admin/')

                if next_page:
                    return redirect(next_page)

            else:
                return render(request, 'login.html', {'form': form, 'message': 'Nie ma takiego uzytkownika'})
        else:
            return render(request, 'login.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            query = User.objects.filter(email=email)

            if query:
                return render(request, 'register.html', {'form':form, 'message': 'Użytkownik o takim mailu istenieje'})

            if password != password2:
                return render(request, 'register.html', {'form':form, 'message': 'Podane hasła nie są identyczne'})

            add_user = User.objects.create(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],
                password2=form.cleaned_data['password2']
            )
            return redirect('/user_registered')

        else:
            return render(request, 'register.html', {'form': form})


class UserRegisteredView(View):
    def get(self, request):
        return render(request, 'user_registered.html', {})