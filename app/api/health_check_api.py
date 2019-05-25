from flask import jsonify

from app.api import api


@api.route("/health-check", methods=["GET"])
def get_health_check():
    """
    Simple health-check, if this is unreachable safe to assume app server has died
    ---
    tags:
      - health-check
    produces:
      - application/json
    responses:
      200:
        description: Service is Healthy
    """
    return jsonify({"status": "healthy"}), 200
