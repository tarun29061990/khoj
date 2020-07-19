FROM python:3.7.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN ["pip", "install", "--upgrade", "pip"]

COPY requirements.txt /usr/src/app/
RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

COPY . /usr/src/app

MAINTAINER Tarun Chaudhary "tarun29061990@gmail.com"
ENV PORT 8000
EXPOSE 8000

WORKDIR /usr/src/app


RUN ["mysite"]

CMD [ "run-program", "uwsgi", "--yaml", "webapp/conf/env/uwsgi.yaml", "--http-socket", "0.0.0.0:8000"]
