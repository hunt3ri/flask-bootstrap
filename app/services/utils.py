from flask import current_app, g
from schematics import Model
from schematics.exceptions import DataError


class FlaskBootstrapError(Exception):
    """
    Custom application exception
    :param message: Error message to log out
    :param error_dict: An optional dict to append to the error, if further info required
    :param status_code: Set the HTTP status code you want the API to return
    """

    def __init__(self, message: str, status_code: int = 500, error_dict: dict = None):
        self.message = message
        self.status_code = status_code

        # Error dict that can be serialized from the API
        self.error = {"errorMessage": message}

        if error_dict:
            self.error.update(error_dict)  # Append error dict to error if available

        current_app.logger.error(self.message)


def validate_dto(dto: Model):
    """ Helper function to validate all DTOs"""
    try:
        dto.validate()
    except DataError as e:
        raise FlaskBootstrapError(
            f"Error validating {type(dto).__name__}", 400, e.to_primitive()
        )


def get_logged_in_user():
    """ Returns the currently logged in user from the session """
    try:
        return g.authenticated_user
    except AttributeError:
        # If we don't have the authenticated user we have set it now
        raise FlaskBootstrapError("No authenticated user in global session")
