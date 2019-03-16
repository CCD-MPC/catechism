#!/bin/bash

cd /app/conclave-web
source backend/venv/bin/activate
gunicorn -b 0.0.0.0:8080 -c /app/conclave-web/config.py -e PYTHONBUFFERED=TRUE wsgi:app