from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from user.forms import UserProfileForm, ChangePasswordForm


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        return render(request, 'user_profile.html', {'user': user})


class UserProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        form = UserProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            })
        return render(request, 'user_profile_form.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            return redirect('user/profile')


class ChangePasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'change_user_password.html', {'form': form})

    def post(self, request):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=request.user.id)
            password = form.cleaned_data['password']
            auth_user = authenticate(username=user.username, password=password)
            if auth_user is not None:
                new_password = form.cleaned_data['new_password']
                re_checked = form.cleaned_data['re_checked']
                if new_password == re_checked:
                    user.set_password(new_password)
                    user.save()
                    return redirect('/')
                else:
                    return render(request, 'change_user_password.html', {'form': form, 'msg': 'Hasła nie są identyczne'})
            else:
                return render(request, 'change_user_password.html', {'form': form, 'msg': 'Podałeś złe hasło bazowe'})
        else:
            return render(request, 'change_user_password.html', {'form': form, 'msg': 'Błędne dane'})
