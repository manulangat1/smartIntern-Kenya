# pull official base image
FROM python:3.8.1-slim-buster

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
ADD . /app
EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:app"]