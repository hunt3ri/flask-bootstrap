FROM python:3.7

RUN apt-get update
RUN apt-get upgrade -y

# App code will be deployed into /src within docker container
WORKDIR /src
ADD . /src

# Add and install Python modules.  Note additional uwsgi install, required to make app windows compatible
RUN pip install --upgrade pip
RUN pip install pipenv; pip install uwsgi
RUN pipenv install --system


# Expose
EXPOSE 8000

# uWSGI used to serve Flask app, configuration loaded from ini file
CMD uwsgi --ini uwsgi.ini
