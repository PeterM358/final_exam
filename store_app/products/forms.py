from django import forms

from store_app.products.models import Product


class BuyProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

