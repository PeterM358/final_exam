from django.template import Library

from store_app.products.models import Product

register = Library()


@register.inclusion_tag('tags/show-products-to-user.html', takes_context=True)
def show_products_to_user(context):
    products = Product.objects.all()
    context['products'] = products
    return context

"""
html
{% for python in pythons %}
            {% include  'pythons/python-details.html' with python=python %}
        {% endfor %}
        
        
        
        


"""