from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from rest_framework.authtoken.models import Token

admin.site.unregister(Group)
admin.site.unregister(Token)

admin.site.site_title = _('Holo-Apollo site admin')
admin.site.site_header = _('Holo-Apollo administration')
