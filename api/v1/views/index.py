#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """status route"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    """stats route"""
    all_objs = storage.all()
    all_objs = len(all_objs)
    all_cls = []
    for obj in all_objs:
        all_cls.append(obj.split('.')[0])
    all_cls = len(set(all_cls))

    return jsonify({"nb_objects": all_objs, "nb_classes": all_cls})
