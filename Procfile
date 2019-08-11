release: ./scripts/release.sh
web: gunicorn config.wsgi --keep-alive 10
worker: celery worker --app=config.celery.app
