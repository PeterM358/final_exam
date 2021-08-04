from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView

UserModel = get_user_model()


class ProfileDetailsView(DetailView):
    model = UserModel
    template_name = 'profiles/view-profile.html'
    context_object_namproductse = 'profile'
