from .base import *  # noqa: F401 F403

API_URL = 'https://holo-crm-test.herokuapp.com'
UI_URL = 'https://holo-site-test.herokuapp.com'

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media-development'

CORS_ORIGIN_REGEX_WHITELIST = [
    # localhost
    r'^(http://)?(localhost|127\.0\.0\.1)(:\d+)?$',

    # test or review heroku app
    r'^(https?://)?(\w+\.)?holo-site-test(-pr-\d+)?\.herokuapp\.com$',
]
