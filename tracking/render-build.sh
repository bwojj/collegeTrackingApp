#!/usr/bin/env bash

# Abort the build immediately if any command fails.
set -o errexit

# Run all build steps from the Django project root.
cd "$(dirname "$0")"

# Install project dependencies and gather static assets for WhiteNoise.
pip install -r requirements.txt
python manage.py collectstatic --noinput
