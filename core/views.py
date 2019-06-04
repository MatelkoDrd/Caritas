from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from core.forms import LoginForm


class BaseView(View):
    def get(self,request):
        return render(request,'base.html', {})


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = request.GET.get('next')
        print(next_page)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

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
