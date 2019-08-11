from .base import *  # noqa: F401 F403

API_URL = 'https://holo-crm-staging.herokuapp.com'
UI_URL = 'https://holo-site-staging.herokuapp.com'

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media-staging'

CORS_ORIGIN_WHITELIST = [
    'https://holo-site-staging.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = CORS_ORIGIN_WHITELIST
