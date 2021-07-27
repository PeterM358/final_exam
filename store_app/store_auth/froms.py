from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email',)


class SignInForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ('username', )