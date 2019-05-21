FROM python:3.7-slim-stretch

RUN apt-get update
RUN apt-get upgrade -y

# App code will be deployed into /src within docker container
WORKDIR /src

# Add and install Python modules.  Note additional uwsgi install, required as not windows compatible
ADD requirements.txt /src/requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt; pip3 install uwsgi
ADD . /src

# Expose
EXPOSE 8000

# uWSGI used to serve Flask app, configuration loaded from ini file
CMD uwsgi --ini uwsgi.ini
