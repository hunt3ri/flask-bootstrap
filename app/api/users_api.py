from flask import jsonify, request, current_app

from app.api import api
from app.models.dtos.user_dto import UserDTO
from app.services.user_service import UserService
from app.services.utils import validate_dto, FlaskBootstrapError


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
        return UserService().register_user(dto), 201
    except FlaskBootstrapError as e:
        current_app.logger.error(e.message)
        return jsonify(e.error), e.status_code
    except Exception as e:
        error_message = f'Unhandled exception: {str(e)}'
        current_app.logger.critical(error_message)
        return jsonify({"errorMessage": error_message}), 500
