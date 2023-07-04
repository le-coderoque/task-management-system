#!/bin/sh

# Wait for the DB to be ready
while ! nc -z db 3306; do
  echo "Waiting for the MySQL Server"
  sleep 3
done

echo "MySQL Server is up - executing command"

python manage.py migrate --noinput
python manage.py createsu
python manage.py collectstatic --noinput
python manage.py test -v1
gunicorn -b 0.0.0.0:8000 task_manager.wsgi:application
