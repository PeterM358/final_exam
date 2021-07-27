from django.urls import path

from store_app.store_auth.views import SignUpView, SignInView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    # path('sign-out/', ),
]