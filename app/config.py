import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class EnvironmentConfig:
    """ Environment Config contains values for the Dev, Test, Prod environments the app runs on. """

    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "flask_bootstrap.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(EnvironmentConfig):
    """ Config for Production environment """

    LOG_DIR = "/var/log/mapfish-py"


class DevConfig(EnvironmentConfig):
    """ Config for Development environment """

    LOG_DIR = "logs"
