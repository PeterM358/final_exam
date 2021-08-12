from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
# from django.contrib.auth.models import User

StoreUser = get_user_model()
#
#
# # class StoreTestCase(TestCase):
# #     def assertListEmpty(self, ll):
# #         return self.assertListEmpty([], ll)
#
#


class ProfileDetailsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = StoreUser.object.create_user(email='koko@abv.bg', password='asdf')

    def test_getDetails_whenLoggedInUser_shouldGet_Details(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('show profile'))

        profile = response.content['profile']

        # self.assertListEmpty()
        self.assertEqual(self.user.id, profile.user_id)


