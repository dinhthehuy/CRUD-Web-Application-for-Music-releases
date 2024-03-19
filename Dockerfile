FROM python:3.11.4-slim-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
