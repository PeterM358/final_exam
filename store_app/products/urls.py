from django.urls import path

from store_app.products.views import IndexView, DeleteProductView, ShowProductsView, CreateProductView, UpdateProductView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('show_products/', ShowProductsView.as_view(), name='show products'),
    path('create_product/', CreateProductView.as_view(), name='create product'),
    path('update_product/<int:pk>', UpdateProductView.as_view(), name='update product'),
    path('delete_product/<int:pk>', DeleteProductView.as_view(), name='delete product')
]