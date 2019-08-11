from django.test import TestCase

from .factories import UserFactory


class TestUser(TestCase):
    def setUp(self):
        self.user = UserFactory(first_name='Jane', last_name='Doe')

    def test_short_name(self):
        self.assertEqual(self.user.get_short_name(), 'Jane')

    def test_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Jane Doe')

    def test_repr(self):
        self.assertEqual(str(self.user), f'Jane Doe {self.user.email}')
