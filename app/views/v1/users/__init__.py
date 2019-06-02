from flask.blueprints import Blueprint

v1_users = Blueprint('v1_users', __name__)

from .controllers import *
