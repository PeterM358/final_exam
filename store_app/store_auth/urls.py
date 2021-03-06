from django.urls import path

from store_app.store_auth.views import SignUpView, SignInView, SignOutView, ListUsersView, UpdateUserView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out', SignOutView.as_view(), name='sign out'),
    path('list-users/', ListUsersView.as_view(), name='list users'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='update user'),
]
