"""import flask views and import storage engine and classes"""
from flask import Blueprint
from models.review import Review
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models import storage
from api.v1.views.places_search import *
from api.v1.views.cities import *
from api.v1.views.states import *
from api.v1.views.places_amenities import *
from api.v1.views.places_reviews import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.places import *
from api.v1.views.index import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
