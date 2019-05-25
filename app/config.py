import logging


class EnvironmentConfig:
    """ Environment Config contains values for the Dev, Test, Prod environments the app runs on. """

    LOG_LEVEL = logging.DEBUG


class ProdConfig(EnvironmentConfig):
    """ Config for Production environment """

    LOG_DIR = "/var/log/mapfish-py"


class DevConfig(EnvironmentConfig):
    """ Config for Development environment """

    LOG_DIR = "logs"
