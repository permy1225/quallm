FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install celery redis

COPY . /app