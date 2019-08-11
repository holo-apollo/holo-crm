from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.common import validators


class TestValidators(TestCase):
    def test_phone_validator(self):
        validator = validators.PhoneValidator()
        self.assertRaises(ValidationError, validator, 'abc')
        self.assertIsNone(validator('+380991234567'))
        self.assertIsNone(validator('(044) 123-23-55'))
