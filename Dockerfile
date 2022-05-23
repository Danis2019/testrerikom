# our base image
FROM python:3.9.13-slim-buster

ADD . /

WORKDIR /

RUN python -m pip install Django
RUN python -m pip install djangorestframework
# specify the port number the container should expose
EXPOSE 8000

# run the application
CMD python manage.py runserver 127.0.0.1:8000