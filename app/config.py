import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class EnvironmentConfig:
    """ Environment Config contains values for the Dev, Test, Prod environments the app runs on. """

    LOG_LEVEL = logging.DEBUG
    SECRET_KEY = os.getenv("FLASK_SECRET")  # Used to generate entropy in tokens etc
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "APP_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "flask_bootstrap.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(EnvironmentConfig):
    """ Config for Production environment """

    LOG_DIR = "/var/log/flask_bootstrap"


class TestConfig(EnvironmentConfig):
    """ Config for unit testing """

    LOG_DIR = "logs"
    SECRET_KEY = "forTestingOnly"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "test_bootstrap.db")
    TESTING = True


class DevConfig(EnvironmentConfig):
    """ Config for Development environment """

    LOG_DIR = "logs"
