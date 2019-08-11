from .staging import *  # noqa: F401 F403

DEBUG = False
ALLOWED_HOSTS = [
    'holo-apollo.art',
    'www.holo-apollo.art',
    'api.holo-apollo.art',
    'holo-site.herokuapp.com',
    'holo-crm.herokuapp.com',
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

API_URL = 'https://api.holo-apollo.art'
UI_URL = 'https://www.holo-apollo.art'

# AWS
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

CORS_ORIGIN_WHITELIST = [
    'https://holo-site.herokuapp.com',
    'https://www.holo-apollo.art',
    'https://holo-apollo.art',
]

CORS_ORIGIN_REGEX_WHITELIST = []
