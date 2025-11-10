#!/usr/bin/env sh
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn project.wsgi:application -w ${GUNICORN_WORKERS:-4} -b 0.0.0.0:8000 --timeout ${GUNICORN_TIMEOUT:-60}

