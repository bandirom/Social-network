#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python /usr/src/web/manage.py makemigrations
python /usr/src/web/manage.py migrate
python /usr/src/web/manage.py createsuperuser --email bandirom@ukr.net --username bandirom

exec "$@"

