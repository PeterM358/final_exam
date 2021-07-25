from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from store_app.common.form_mixin import BootStrapFormViewMixin
from store_app.products.models import Product


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'BEST PRICES'
        }


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


class CreateProductView(BootStrapFormViewMixin, CreateView):
    model = Product
    template_name = 'products/create_products.html'
    fields = '__all__'
    success_url = reverse_lazy('show products')
    # form_class = ProductForm


class UpdateProductView(UpdateView):
    model = Product
    template_name = 'products/update_products.html'
    fields = '__all__'
    success_url = reverse_lazy('show products',)


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/delete_products.html'
    success_url = reverse_lazy('show products')


class ShowProductsView(ListView):
    model = Product
    template_name = 'products/show_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_title'] = 'Product title'
        return context
