#!/bin/sh

docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

exec "$@"

