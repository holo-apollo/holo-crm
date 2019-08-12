from django.test import TestCase

from .factories import CustomerFactory


class CustomerTestCase(TestCase):
    def test_str(self):
        customer = CustomerFactory(name='Jeff D-oh', email='doh@ha.art')
        self.assertEqual(str(customer), 'Jeff D-oh <doh@ha.art>')
