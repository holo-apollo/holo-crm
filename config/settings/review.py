from .base import *  # noqa: F401 F403

STATICFILES_LOCATION = 'static-review'
MEDIAFILES_LOCATION = 'media-review'

CORS_ORIGIN_REGEX_WHITELIST = [
    # localhost
    r'^(http://)?(localhost|127\.0\.0\.1)(:\d+)?$',

    # test or review heroku app
    r'^(https?://)?(\w+\.)?holo-site-test(-pr-\d+)?\.herokuapp\.com$',
]
