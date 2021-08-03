from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from store_app.common.mixins import BootStrapFormViewMixin, AnyGroupRequiredMixin
from store_app.products.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     return {
    #         'title': 'BEST PRICES'
    #     }


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


class CreateProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'products/create_products.html'
    fields = '__all__'
    success_url = reverse_lazy('show products')
    # form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class UpdateProductView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  #TODO fix roles
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


class ShowProductsView(ListView):
    model = Product
    template_name = 'products/show_products.html'
    context_object_name = 'products'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['product_title'] = 'Product title'
    #     return context


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'


class BuyProductView(): #TODO
    pass