import os
import warnings

from base64 import b64encode
from time import time

import click

from app import bootstrap_app, db
from app.services.auth_service import get_session_token, JWTSessionUser, SESSION_TIMEOUT


# Warn if any of required environment vars have not been set
for var in ["FLASK_SECRET"]:
    if not os.getenv(var):
        warnings.warn(f"{var} environment variable must be set")

app = bootstrap_app()  # Initialise the Flask app


@app.shell_context_processor
def make_shell_context():
    """
    Make sqlalchemy db object available to the cli, enables us to run db migrations as follows:
    > flask db init       # Initialise migrations
    > flask db migrate    # Create migration
    > flask db upgrade    # Upgrade the database
    > flask db downgrade  # Downgrade the database by 1 migration
    """
    return {'db': db}


@app.cli.command()
@click.option('--username', default='iain', help='Username for user')
@click.option('--password', default='password', help='Password for the user')
def gen_basic_auth(username, password):
    """
    Helper to generate a valid basic authentication header for supplied username and pass.
    To run, from commandline:  flask gen-basic-auth
    Or to run with options:  flask gen-basic-auth --username abi --password pass123
    """
    print('Generating Base64 encoded Basic Authentication token copy and paste to Swagger...')
    auth_details = f'{username}:{password}'.encode('utf-8')

    base64string = b64encode(auth_details)
    print(f"Basic {base64string.decode('utf-8')}")


@app.cli.command()
@click.option('--userid', default='1', help='Userid for user')
def gen_session_token(userid: int):
    """
    Helper to generate a valid session token header for supplied userid
    To run, from commandline:  flask gen-session-token
    Or to run with options:  flask gen-session-token --userid 12
    """
    print('Generating Session token copy and paste to Swagger...')
    session_user = JWTSessionUser()
    session_user.id = userid
    session_user.first_name = "FlaskGen"
    session_user.exp = time() + SESSION_TIMEOUT
    token = get_session_token(session_user)

    print(f"Bearer {token}")
