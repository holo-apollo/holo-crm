from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.common.fields import PhoneField
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    username = models.CharField(
        verbose_name=_('Username'),
        max_length=30,
        unique=True,
        error_messages={
            'unique': _('That username is already taken.')
        }
    )
    first_name = models.CharField(
        verbose_name=_('First name'),
        max_length=30,
        blank=True,
        default=''
    )
    last_name = models.CharField(
        verbose_name=_('Last name'),
        max_length=30,
        blank=True,
        default=''
    )

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

    is_staff = models.BooleanField(
        verbose_name=_('Staff status'),
        default=False
    )
    is_active = models.BooleanField(
        verbose_name=_('Active status'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )
    last_updated = models.DateTimeField(
        verbose_name=_('Last updated'),
        auto_now=True
    )
    avatar = models.URLField(verbose_name=_('Avatar'), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.get_full_name()} {self.email}'

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    get_full_name.short_description = _('Full name')
