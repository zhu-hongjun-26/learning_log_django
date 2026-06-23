#!/bin/bash
echo "Starting Gunicorn..."
gunicorn ll_project.wsgi:application --bind 0.0.0.0:$PORT