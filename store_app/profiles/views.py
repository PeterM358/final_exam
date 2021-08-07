from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from store_app.profiles.forms import UpdateProfileForm, AddCashForm
from store_app.profiles.models import Profile, Cart

UserModel = get_user_model()


class ShowProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profiles/show-profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.get(pk=self.request.user.id)
        context['profile'] = Profile.objects.get(pk=self.request.user.id)
        return context


class UpdateProfileView(UpdateView):
    model = Profile
    template_name = 'profiles/update-profile.html'
    form_class = UpdateProfileForm
    # success_url = reverse_lazy('show profile')

    # giving id to detailview THIS WORKsS
    def get_success_url(self):
        return redirect('show profile')
    # kwargs={'pk': self.request.user.id}


def add_cash(request):
    cart = Cart.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = AddCashForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(pk=request.user.id)
            amount = form.cleaned_data['amount']
            cart.cash += amount
            cart.save()
            profile.save()
            return redirect('index')
    else:
        form = AddCashForm(request.POST)
    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'profiles/add-money.html', context)