#!/bin/bash

cd /app/chamberlain
gunicorn -b 0.0.0.0:8080 -c /app/chamberlain/config.py -e PYTHONBUFFERED=TRUE wsgi:app
