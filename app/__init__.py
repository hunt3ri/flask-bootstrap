import logging
import os

from logging.handlers import RotatingFileHandler

from flasgger import Swagger
from flask import Flask

# Update with app specific versions as needed
APP_NAME = 'FLASK-BOOTSTRAP'
APP_VERSION = 'v1'

# Init dependencies
swagger = Swagger()


def bootstrap_app() -> Flask:
    """ Bootstrap function to initialise the Flask app and config """
    app = Flask(__name__)
    set_config(app)

    initialise_logger(app)
    app.logger.info('Mapfish-PY Starting Up, Environment = {0}'.format(get_current_environment()))

    register_flask_blueprints(app)
    init_swagger_docs(app)

    return app


def set_config(app: Flask):
    """ Sets the config for the current environment """
    env = get_current_environment()
    app.config.from_object('app.config.{0}Config'.format(env))


def get_current_environment() -> str:
    """ Gets the currently running environment from the OS Env Var """
    env = os.getenv(APP_NAME, 'Dev')  # default to Dev if config environment var not set
    return env.capitalize()


def initialise_logger(app: Flask):
    """ Read environment config then initialise a 2MB rotating log. """
    log_dir = app.config['LOG_DIR']
    log_level = app.config['LOG_LEVEL']

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create 2Mb Rotating Log
    file_handler = RotatingFileHandler(log_dir + f'/{APP_NAME}.log', 'a', 2 * 1024 * 1024, 3)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    app.logger.addHandler(file_handler)
    app.logger.setLevel(log_level)


def register_flask_blueprints(app: Flask):
    """ Register all flask blueprints.  Note need to import code here to avoid circular dependency issues """
    # API blueprint
    from app.api import api as api_bp
    app.register_blueprint(api_bp, url_prefix=f'/api/{APP_VERSION}')

    # Web blueprint for html pages
    from app.web import main as main_bp
    app.register_blueprint(main_bp)


def init_swagger_docs(app: Flask):
    """ Initialise the swagger API docs using the flasgger lib.  Docs are available at /apidocs """
    app.config['SWAGGER'] = {
        'title': f'{APP_NAME} API',
        'uiversion': 3,
        "version": f"{APP_VERSION}"
    }
    swagger.init_app(app)
