from flask import Blueprint

api = Blueprint("api", __name__, template_folder="api_templates", url_prefix="/api")

from . import routes
