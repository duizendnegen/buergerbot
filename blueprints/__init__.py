from flask import Blueprint

anmeldung = Blueprint('anmeldung', __name__)

from web_app.routes import *
from web_app.events import *