from django.db import models


class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=200,
    )
    price = models.IntegerField()
    product_image = models.ImageField(
        upload_to='product_images',
        blank=True,
        null=True,
    )

    CATEGORIES = (
        (1, 'Electronics'),
        (2, 'Furniture'),
        (3, 'Kids staff')
    )

    category = models.BooleanField(
        choices=CATEGORIES,

    )

