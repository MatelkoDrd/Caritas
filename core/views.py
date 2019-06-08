from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from core.forms import LoginForm
from core.forms import RegisterForm
from user.models import User


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html', {})


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
                if next_page:
                    return redirect(next_page)
                return redirect('/')
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
            return render(request, 'register.html', {'form': form, 'message': f"Stworzono nowego użytkownika{add_user}"})

        else:
            return render(request, 'register.html', {'form': form})