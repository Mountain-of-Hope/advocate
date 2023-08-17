#!/bin/bash

source /var/app/venv/*/bin/activate && {

# collecting static files
python manage.py collectstatic --noinput;
# log which migrations have already been applied
python manage.py makemigrations;
# migrate the rest
python manage.py migrate --noinput;
}