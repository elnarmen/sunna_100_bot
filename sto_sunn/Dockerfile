# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt sto_sunn/requirements.txt

RUN pip3 install --upgrade pip
RUN pip install -r sto_sunn/requirements.txt

COPY .. .
