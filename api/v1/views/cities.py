#!/usr/bin/python3

"""Create a new City view to handle all default REST API functionality"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import city
from models.engine import storage

@app_views.route('/api/v1/states/<state_id>/cities', methods=["GET"], strict_slashes=False)
def get_city(state_id):
    """A List of Cities in a State"""
    obj_list = []
    city_list = storage.all("City")
    for obj in city_list.get(str(state_id)):
        if obj is None:
            return abort(404)
        else:
            return jsonify(obj_list.append(obj))


@app_views.route('/api/v1/cities/<city_id>', methods=["GET"], strict_slahes=False)
def get_city_id(city_id):
    """Retrieves a City by city_id"""
    city_obj = storage.get("City", str(city_id))
    if city_obj is None:
        return abort(404)
    else:
        return jsonify(city_obj)


@app_views.route('/api/v1/cities/<city_id>', methods=["DELETE"], strict_slashes=False)
def delete_city(city_id):
    """Delete a City by city id"""
    city_obj = storage.get("City", str(city_id))
    if city_obj is None:
        return abort(404)
    else:
        storage.delete(city_obj)
        storage.save()
        return jsonify({})
