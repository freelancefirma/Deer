#!/usr/bin/env bash
rm -rf staticfiles/
python manage.py collectstatic --noinput
