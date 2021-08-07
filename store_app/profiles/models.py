from django.contrib.auth import get_user_model
from django.db import models

from store_app.products.models import Product
from store_app.store_auth.models import StoreUser

UserModel = get_user_model()


class Profile(models.Model):

    def __str__(self):
        return f'profile: {self.first_name}'

    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profile_images',
        blank=True,
    )

    user = models.OneToOneField(
        StoreUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Cart(models.Model):

    def __str__(self):
        return f'Cart - user_id:{self.user_id}'

    products = models.ManyToManyField(
        Product,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        blank=True,
        on_delete=models.CASCADE,
    )




