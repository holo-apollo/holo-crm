from django.conf import settings


def settings_vars(request):
    return {'PRODUCTION': settings.PRODUCTION}
