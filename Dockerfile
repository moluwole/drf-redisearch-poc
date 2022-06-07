FROM python:3.9.6-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt

RUN pip install --no-cache-dir -r requirements-dev.txt


COPY . /usr/src/app