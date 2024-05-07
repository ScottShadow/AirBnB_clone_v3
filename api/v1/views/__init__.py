#!/usr/bin/python3
"""import flask views and import storage engine and classes"""

from flask import Blueprint
from models import storage
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
