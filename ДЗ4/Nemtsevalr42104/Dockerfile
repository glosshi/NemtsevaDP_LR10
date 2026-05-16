FROM python:3.11-slim

WORKDIR /app

# Ставим системные пакеты, нужные для сборки mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install django gunicorn mysqlclient

EXPOSE 8000

CMD ["gunicorn", "django_project.wsgi:application", "--bind", "0.0.0.0:8000"]
