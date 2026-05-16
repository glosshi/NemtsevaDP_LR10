#!/bin/bash
set -e

echo "=== Применение миграций базы данных ==="
python manage.py migrate

echo "=== Запуск Django-приложения на 0.0.0.0:3000 ==="
python manage.py runserver 0.0.0.0:3000