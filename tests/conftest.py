import os
import pytest

from flask_migrate import upgrade, downgrade

from app import bootstrap_app


@pytest.fixture
def app():
    """ Create and configure a new app instance for each test """
    app = bootstrap_app(env='Test')

    # Work out where DB migrations are living so we can apply them
    tests_dir = os.path.dirname(os.path.realpath(__file__))
    migrations_dir = os.path.join(tests_dir, "..", "migrations")

    with app.app_context():
        #downgrade(directory=migrations_dir)
        upgrade(directory=migrations_dir)
    yield app

    iain = 1


@pytest.fixture()
def client(app):
    """ A test client for the app """
    return app.test_client()
