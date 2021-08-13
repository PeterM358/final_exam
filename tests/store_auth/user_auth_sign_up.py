from django.contrib.auth import get_user_model
from django.test import TestCase


from store_app.profiles.models import Profile, Cart

StoreUser = get_user_model()


class UserCreateTest(TestCase):
    def setUp(self):
        self.user = StoreUser.objects.create_user(email='koko@abv.bg', password='asdf')

    def test_createCustomUser_shouldBeCreated(self):
        self.assertEqual('koko@abv.bg', self.user.email)

    def test_autoProfileCreated_whenUserCreate_shouldBeCreated(self):
        profile = Profile.objects.get(pk=self.user.id)

        self.assertEqual('', profile.first_name)
        self.assertEqual('', profile.last_name)
        self.assertEqual(None, profile.age)
        self.assertEqual(profile.user_id, self.user.id)

    def test_autoCartCreated_whenUserCreate_shouldBeCreated(self):
        cart = Cart.objects.get(pk=self.user.id)

        self.assertEqual(cart.id, self.user.id)
        self.assertEqual(0, cart.cash)

