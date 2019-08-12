from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from apps.common.fields import PhoneField


class Customer(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=50)
    email = CIEmailField(
        verbose_name=_('Email'),
        max_length=254,
        unique=True,
        error_messages={
            'unique': _('That email address is already taken.')
        }
    )
    phone = PhoneField(
        verbose_name=_('Phone'),
        blank=True,
        default='',
        unique=True,
        error_messages={
            'unique': _('That phone number is already taken.')
        }
    )

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return f'{self.name} <{self.email}>'
