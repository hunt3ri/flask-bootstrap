from flask import jsonify, request, current_app

from app.api import api
from app.models.dtos.user_dto import UserDTO
from app.services.auth_service import basic_auth, token_auth
from app.services.user_service import UserService
from app.services.utils import validate_dto, FlaskBootstrapError, get_logged_in_user


@api.route("/user/register", methods=["POST"])
def register_user():
    """
    Register a new user
    ---
    tags:
      - user
    parameters:
      - in: body
        name: body
        required: true
        description: JSON object for creating a new user
        schema:
          "$ref": "#/definitions/User"
    definitions:
      User:
        description: "Models a User"
        type: object
        properties:
          firstName:
            type: string
            example: Iain
          lastName:
            type: string
            example: Hunter
          password:
            type: string
            example: "}<+4v@J6nk"
          email:
            type: string
            example: "email@address.com"
    responses:
      201:
        description: User created
      400:
        description: Bad Request
      500:
        description: Internal Server Error
    """
    try:
        dto = UserDTO(request.get_json())
        validate_dto(dto)
        registered_user = UserService().register_user(dto)
        return jsonify(registered_user.to_primitive()), 201
    except FlaskBootstrapError as e:
        current_app.logger.error(e.message)
        return jsonify(e.error), e.status_code
    except Exception as e:
        error_message = f"Unhandled exception: {str(e)}"
        current_app.logger.critical(error_message)
        return jsonify({"errorMessage": error_message}), 500


@api.route("/user/login", methods=["PUT"])
@basic_auth.login_required
def login_user():
    """
    Login User
    ---
    tags:
      - user
    produces:
      - application/json
    parameters:
      - in: header
        name: Authorization
        description: Base64 encoded user password
        required: true
        type: string
    responses:
      200:
        description: Login Successful
      401:
        description: Unauthorized, credentials are invalid
      500:
        description: Internal Server Error
    """
    try:
        logged_in_user = get_logged_in_user()
        return jsonify(logged_in_user.to_primitive()), 200
    except FlaskBootstrapError as e:
        current_app.logger.error(e.message)
        return jsonify(e.error), e.status_code
    except Exception as e:
        error_message = f"Unhandled exception: {str(e)}"
        current_app.logger.critical(error_message)
        return jsonify({"errorMessage": error_message}), 500


@api.route("/user/<int:user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id: int):
    """
    Get user info
    ---
    tags:
      - user
    produces:
      - application/json
    parameters:
      - in: header
        name: Authorization
        description: Base64 encoded user password
        required: true
        type: string
      - in: path
        name: user_id
        description: User ID
        type: int
        example: 1
    responses:
      200:
        description: Login Successful
      401:
        description: Unauthorized, credentials are invalid
      500:
        description: Internal Server Error
    """
    try:
        logged_in_user = get_logged_in_user()
        return jsonify(logged_in_user.to_primitive()), 200
    except FlaskBootstrapError as e:
        current_app.logger.error(e.message)
        return jsonify(e.error), e.status_code
    except Exception as e:
        error_message = f"Unhandled exception: {str(e)}"
        current_app.logger.critical(error_message)
        return jsonify({"errorMessage": error_message}), 500
