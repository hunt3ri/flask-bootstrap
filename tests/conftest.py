import pytest
from app import bootstrap_app


@pytest.fixture
def app():
    """ Create and configure a new app instance for each test """
    app = bootstrap_app()
    yield app
