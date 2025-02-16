#!/bin/bash

poetry run sleep 5

poetry run alembic upgrade head

poetry run python3 -m seeds.seed

poetry run gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind="0.0.0.0:8000" --access-logfile - --error-logfile - --log-level info
