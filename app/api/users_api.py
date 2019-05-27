from flask import jsonify

from app.api import api


@api.route("/user/register", methods=["POST"])
def register_user():
    """
    Simple health-check, if this is unreachable safe to assume app server has died
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
                emailAddress:
                    type: string
                    example: "email@address.com"
    responses:
      201:
        description: User Created
      400:
        description: Bad Request
      500:
        description: Internal Server Error
    """
    return jsonify({"status": "healthy"}), 201
