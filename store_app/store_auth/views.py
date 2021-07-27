from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from store_app.store_auth.froms import SignUpForm, SignInForm

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SignInView(View):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm
