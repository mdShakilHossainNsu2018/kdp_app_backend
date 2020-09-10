release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn kdp_app_backend.wsgi --log-file -

