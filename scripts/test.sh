#!/usr/bin/env bash

flake8 apps/
ret_code_flake=$?

python manage.py test
ret_code_django_test=$?

if [ $ret_code_flake != 0 ] || [ $ret_code_django_test != 0 ] ; then
  exit 1
fi
