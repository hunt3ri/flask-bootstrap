from flask import Blueprint

api = Blueprint('api', __name__)

from app.api import health_check_api
