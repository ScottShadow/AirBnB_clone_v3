#!/usr/bin/python3
"""
starts a Flask web application for the AirBnb project
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status route"""
    data = {
        "status": "OK"
    }

    resp = jsonify(data)
    resp.status_code = 200

    return resp


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def storage_counts():
    """
        return counts of all classes in storage
    """
    cls_counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    resp = jsonify(cls_counts)
    resp.status_code = 200

    return resp
