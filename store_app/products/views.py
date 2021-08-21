from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from store_app.products.models import Product
from store_app.profiles.models import Cart


UserModel = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'


class CreateProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'products/create_products.html'
    fields = '__all__'
    success_url = reverse_lazy('show products')

    # form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateProductView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Only staff members and super user have rights to update -> test_func
    '''
    model = Product
    template_name = 'products/update_products.html'
    fields = '__all__'
    success_url = reverse_lazy('show products', )

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class DeleteProductView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'products/delete_products.html'
    success_url = reverse_lazy('show products')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class ShowProductsView(ListView):
    model = Product
    template_name = 'products/show_products.html'
    context_object_name = 'products'
    pagination = 4

    def get_context_data(self, **kwargs):
        context = super(ShowProductsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'


def buy_product(request, pk):
    # getting product and user cart
    product = Product.objects.get(pk=pk)
    cart = Cart.objects.get(pk=request.user.id)
    if cart.cash - product.price > 0:
        cart.cash -= product.price
        cart.products.add(product)
        cart.save()
        return render(request, 'profiles/show-profile.html', {'cart': cart})
    return HttpResponse('You dont have enough money')