#!/bin/sh

docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser

exec "$@"

