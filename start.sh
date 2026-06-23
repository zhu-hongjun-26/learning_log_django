#!/bin/bash
python manage.py migrate
gunicorn ll_project.wsgi:application --bind 0.0.0.0:$PORT