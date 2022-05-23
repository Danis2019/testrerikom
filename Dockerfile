# our base image
FROM python:3-onbuild

# specify the port number the container should expose
EXPOSE 8000

# run the application
CMD ["python", "manage.py runserver"]