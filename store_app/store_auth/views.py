from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from store_app.store_auth.froms import SignUpForm, SignInForm
from store_app.store_auth.models import StoreUser

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'auth/sign-up.html'
    # model = UserModel
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    # autologin user
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(LoginView):
    template_name = 'auth/sign-in.html'
    form_class = SignInForm

    def get_success_url(self):
        return reverse_lazy('index')


class SignOutView(LogoutView):
    template_name = 'auth/sign-out.html'
    next_page = reverse_lazy('index')


class ListUsersView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'auth/list_users.html'
    model = StoreUser
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    # def get_queryset(self):
    #     return StoreUser.object.all()


class UpdateUserView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserModel
    template_name = 'auth/update_user.html'
    fields = ('is_staff',)
    success_url = reverse_lazy('list users')
    # slug_field = 'url'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        return context




