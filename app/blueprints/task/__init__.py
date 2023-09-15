from flask import Blueprint

pages = Blueprint("pages", __name__, template_folder="pages_templates")

from . import routes
