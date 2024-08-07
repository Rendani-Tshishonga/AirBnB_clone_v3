#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models.engine import storage

@app_views.route('/status', strict_slashes=False)
def status():
    """ A method to return status okay"""
    data = {'status': 'ok'}
    response = jsonify(data)
    return response

@app_views.route('/stats', strict_slashes=False)
def obj_count():
    """Retrieves the count of all objects"""
    data = {
        "amenities": storage.count("Amenity"),
        "cites": storage.count("City"),
        "places": storage.count("Place"),
        "review": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
            }
    response = jsonify(data)
    return response
