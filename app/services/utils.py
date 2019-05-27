from flask import current_app
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
        if current_app:
            current_app.logger.error(message)

        # Error object that can be serialized from the API
        self.error = {
            "errorMessage": message
        }

        if error_dict:
            self.error.update(error_dict)  # Append error dict to error if available

        self.status_code = status_code


def validate_dto(dto: Model):
    """ Helper function to validate all DTOs"""
    try:
        dto.validate()
    except DataError as e:
        raise FlaskBootstrapError(f"Error validating {type(dto).__name__}", 400, e.to_primitive())


def unhandled_exception(error: Exception):
    """ Helper function to handle unhandled exceptions """
    error_message = f'Unhandled exception: {str(error)}'
    current_app.logger.critical(error_message)
    return {"errorMessage": error_message}, 500
