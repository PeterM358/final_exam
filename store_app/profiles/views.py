from django.contrib.auth import get_user_model

from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from store_app.profiles.forms import UpdateProfileForm
from store_app.profiles.models import Profile, Cart

UserModel = get_user_model()


class ShowProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/show-profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.get(pk=self.request.user.id)
        return context


class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/update-profile.html'
    form_class = UpdateProfileForm
    # success_url = reverse_lazy('show profile')

    # giving id to detailview THIS WORKsS
    def get_success_url(self):
        return reverse('show profile', args=[self.kwargs['pk']])
    # kwargs={'pk': self.request.user.id}
