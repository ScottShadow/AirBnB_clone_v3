"""import flask views and import storage engine and classes"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from models import storage
from api.v1.views.index import *

