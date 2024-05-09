#!/usr/bin/python3
"""import flask views and import storage engine and classes"""

from flask import Blueprint
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import * 
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
