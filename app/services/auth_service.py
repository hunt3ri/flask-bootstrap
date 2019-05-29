from flask import g
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

basic_auth = HTTPBasicAuth()


@basic_auth.verify_password
def verify_credentials(username: str, password: str) -> bool:
    """ Verify username and password are valid """
    user = UserService().get_user_by_email(username)

    if check_password_hash(user.password_hash, password):
        set_auth_details(user)
        return True

    return False


def get_password_hash(password: str):
    """ Creates secure hash of supplied password """
    return generate_password_hash(password)


def set_auth_details(user):
    """ Set user details into global request scope for later retrieval """
    # TODO generate session token
    dto = UserDTO().map_from_db_model(user)
    dto.password = None  # Never store/return password
    g.authenticated_user = dto


from app.services.user_service import (
    UserService,
    UserDTO,
)  # noqa avoid circular dependency
