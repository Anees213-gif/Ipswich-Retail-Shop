web: cd backend && python manage.py migrate && python manage.py collectstatic --noinput && python manage.py load_sample_data && gunicorn --bind 0.0.0.0:$PORT ipswich_retail.wsgi:application
