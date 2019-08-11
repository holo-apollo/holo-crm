from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# TODO: improve it
class PhoneValidator(RegexValidator):
    regex = r'^[-0-9+()\s]*$'
    message = _('Enter a valid phone number')
