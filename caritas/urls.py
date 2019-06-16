"""caritas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from core.views import BaseView, LoginView, RegisterView, UserRegisteredView
from user.views import UserProfileView, UserProfileEditView, ChangePasswordView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('login', LoginView.as_view(), name='login'),
    url('register/', RegisterView.as_view(), name='register'),
    url('user_registered', UserRegisteredView.as_view()),
    url('profile', UserProfileView.as_view()),
    url('profile_form', UserProfileEditView.as_view()),
    url('change_password', ChangePasswordView.as_view()),
    url('', BaseView.as_view(), name='home'),

]
