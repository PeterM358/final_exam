from django.contrib.auth import get_user_model
from django.test import TestCase
from store_app.products.models import Product


StoreUser = get_user_model()


class ProductCreateTest(TestCase):
    def setUp(self):
        self.user = StoreUser.objects.create_user(
            email='koko@abv.bg',
            password='asdf',
            is_superuser=False,
            is_staff=False,
        )

    def test_createProduct_whenNotStaffOrSuperUser_shouldRaise403(self):
        self.client.force_login(self.user)

        response = self.client.get('/create_product/',)

        self.assertEqual(response.status_code, 403)

    def test_createProduct_whenStaffOrSuperUser_shouldResponse200(self):
        self.user = StoreUser.objects.create_user(
            email='koko1@abv.bg',
            password='asdf',
            is_superuser=True,
            is_staff=True,
        )

        self.client.force_login(self.user)

        response = self.client.get('/create_product/')

        self.assertEqual(response.status_code, 200)

    def test_createProduct_whenStaffOrSuperUser_shouldCreateProduct302(self):
        self.user = StoreUser.objects.create_user(
            email='koko1@abv.bg',
            password='asdf',
            is_superuser=True,
            is_staff=True,
        )

        Product.objects.create(
            name='Iphone',
            description='Iphone desc',
            price='100',
            product_image='path/to/image.png',
            category=1,
        )

        response = self.client.post('/create_product/')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 1)
