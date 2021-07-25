from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    product_image = models.ImageField(
        upload_to='product_images',
        blank=True,
        null=True,
    )


## TODO class Like
