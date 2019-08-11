#!/usr/bin/env bash

python manage.py migrate --noinput
# commenting for now since static files aren't going to change
# python manage.py fasts3collectstatic --noinput
