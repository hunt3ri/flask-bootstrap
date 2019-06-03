from time import time

import jwt

from jwt.exceptions import ExpiredSignature
from flask import g, current_app
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.dtos.user_dto import UserDTO, JWTSessionUser

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth("Bearer")

# Number of seconds before session token expires
SESSION_TIMEOUT = 600


@basic_auth.verify_password
def verify_credentials(username: str, password: str) -> bool:
    """ Verify username and password are valid """
    user = UserService().get_user_by_email(username)

    if check_password_hash(user.password_hash, password):
        user_dto = UserDTO().map_from_db_model(user)
        set_auth_details(user_dto)
        return True

    return False


@token_auth.verify_token
def verify_token(token: str) -> bool:
    """ Verifies that the session token is valid """
    try:
        payload = jwt.decode(token, key=current_app.secret_key, algorithms=["HS256"])
        session_user = JWTSessionUser(payload)
        set_session_user(session_user)
        return True
    except ExpiredSignature:
        current_app.logger.warn("Expired signature")
        return False
    except Exception as e:
        current_app.logger.error(f"Unable to decode token, error: {str(e)}")
        return False


def get_password_hash(password: str):
    """ Creates secure hash of supplied password """
    return generate_password_hash(password)


def set_auth_details(user_dto: UserDTO) -> JWTSessionUser:
    """ Set user details into global request scope for later retrieval """
    session_user = JWTSessionUser()
    session_user.id = user_dto.id
    session_user.first_name = user_dto.first_name
    session_user.exp = time() + SESSION_TIMEOUT
    session_user.session_token = get_session_token(session_user)
    set_session_user(session_user)
    return session_user


def get_session_token(session_user: JWTSessionUser):
    """ Generate a JWT to represent the user """
    # NOTE this can be customized as needed, see
    # https://blog.miguelgrinberg.com/post/json-web-tokens-with-public-key-signatures
    token = jwt.encode(
        payload=session_user.to_primitive(),
        key=current_app.secret_key,
        algorithm="HS256",
    ).decode("utf-8")
    return token


def set_session_user(session_user: JWTSessionUser):
    """ Save logged in user in Flask Global object for easy retrieval """
    g.authenticated_user = session_user


from app.services.user_service import UserService  # noqa avoid circular dependency
