from django.urls import path

from store_app.profiles.views import UpdateProfileView, ShowProfileDetailsView

urlpatterns = (
    path('update_prfile/<int:pk>', UpdateProfileView.as_view(), name='update profile'),
    path('<int:pk>', ShowProfileDetailsView.as_view(), name='show profile'),
)

from .signals import *