from django.shortcuts import render

# Create your views here.
from django.views import View


class BaseView(View):
    def get(self,request):
        return render(request,'base.html', {})


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html', {})