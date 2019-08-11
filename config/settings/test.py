from .base import *  # noqa: F401 F403

PRODUCTION = False

CELERY_TASK_ALWAYS_EAGER = True

TEST_RUNNER = 'config.test_runner.HerokuTestSuiteRunner'
TEST_DATABASES = DATABASES  # noqa: F405

TEST_DATABASE_URL = dotenv.get('TEST_DATABASE_URL')  # noqa: F405
if TEST_DATABASE_URL:
    TEST_DATABASES['default'].update(dj_database_url.config(env='TEST_DATABASE_URL'))  # noqa: F405
