#!/usr/bin/python3
"""Create a new view for State objects
that handles all default RESTFul API actions
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.state import State
from models.engine import storage


@app_reviews.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all state objects"""
    list_objects = []
    states_list = storage.all("State")
    from obj in states_list.values():
        list_objects.append(obj)
    return jsonify(list_objects)


@app_reviews.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    """Retrieves a state object"""
    state_obj = storage.get("State", str(state_id))
    if state_obj is None:
        abort(404)
    else:
        return jsonify(state_obj)


@app_reviews.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_states(state_id):
    """Deletes a state object"""
    state_obj = storage.get("State", str(state_id))
    if state_obj is None:
        abort(404)
    else:
        storage.delete(state_obj)
        storage.save()
    return jsonfiy({})


@app_reviews.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Creates a State"""
    request_json = request.get_json()
    if request_json is None:
        abort(404, 'Not a JSON')
    elif "name" is not in request_json.keys():
        abort(400, 'Missing name')
    else:
        new_state = State(**request_json)
        new_state.save()
        response = jsonify(new_state.to_dict())
        
    return response
