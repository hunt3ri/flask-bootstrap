# Flask Bootstrap
This repo contains a skeleton flask project you can use to quickly bootstrap your projects. It's designed to be easily deployed to serverless environments or container clusters (see DevOps below)

Currently we have two branches:
### master
[![Run Status](https://api.shippable.com/projects/5ce50c5c09683700079dafa0/badge?branch=master)]()
[![Coverage Badge](https://api.shippable.com/projects/5ce50c5c09683700079dafa0/coverageBadge?branch=master)]()

Simple Flask App with Restful API documented by Swagger

### flask-bootstrap-sqlite

[![Run Status](https://api.shippable.com/projects/5ce50c5c09683700079dafa0/badge?branch=flask-bootstrap-sqlite)](https://app.shippable.com/github/hunt3ri/flask-bootstrap/dashboard) 
[![Coverage Badge](https://api.shippable.com/projects/5ce50c5c09683700079dafa0/coverageBadge?branch=flask-bootstrap-sqlite)](https://app.shippable.com/github/hunt3ri/flask-bootstrap/dashboard)

Builds on the simple app in master, adds a SQLite DB, user registration and authorisation

## Installing
### Python 3.7+
You need to have at least Python 3.7 installed in your development environment.

### Dependencies 
To install the required dependencies:
```.bash
pip install pipenv
pipenv install --dev
pre-commit install
```
Note the app uses [pre-commit](https://pre-commit.com/) to ensure we automatically run the [black](https://black.readthedocs.io/en/stable/) code formatter and [flake8](http://flake8.pycqa.org/en/latest/) linter before each commit 

## Running Flask Bootstrap

### Create a .env file
Flask-Bootstrap installs [python-dotenv](https://github.com/theskumar/python-dotenv) to manage local environment variables it is strongly advised to create a ```.env``` file in the root of your project to store all environment variables.

### Running
To run ensure your virtual environment is running
```.bash
pipenv shell
flask run
```

### Tests
To run all tests
```bash
pytest tests
```

### API Docs
API docs are generated by [Flasgger](https://github.com/rochacbruno/flasgger) all API methods should be decorated with swagger comments. API docs page can be viewed here:

[http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)

## DevOps
### Docker
Flask-Bootstrap can be built and run from within a Docker container:
```.docker
docker build -t flask-bootstrap .
docker run -d -p 8080:8000 flask-bootstrap
```

You should see the app running locally on port 8080 - [http://127.0.0.1:8080](http://127.0.0.1:8080)

### Useful commands:

```.docker
# Connect to the running container
docker exec -it <imageId> bash
```

### CI
Flask-Bootstrap CI is run by [Shippable](https://www.shippable.com/). New CI scripts can be added within the ```devops``` dir 