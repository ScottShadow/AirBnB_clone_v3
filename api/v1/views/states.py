#!/usr/bin/python3
'''
    RESTful API for class State
'''
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """
    Returns a list of all states in JSON format.

    Returns:
        A JSON object containing a list of all states.
    """
    # Retrieve all states from storage and convert them to dictionaries
    state_list = [s.to_dict() for s in storage.all('State').values()]

    # Return the state list as a JSON response
    return jsonify(state_list)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state_id(state_id):
    '''
        Return a state and its id using the HTTP verb GET.

        Args:
            state_id (str): The id of the state object to retrieve.

        Returns:
            A JSON object representing the state object with the given id.

        Raises:
            404 Not Found: If the state object with the given id is not found.
    '''
    # Retrieve the state object from storage based on the given id
    state = storage.get("State", state_id)

    # If the state object is not found, return a 404 error
    if state is None:
        abort(404)

    # Return the state object as a JSON response
    return jsonify(state.to_dict())


@app_views.route(
    '/states/<state_id>',
    methods=['DELETE'],
    strict_slashes=False)
def delete_state(state_id):
    '''
        DELETE a state object by its id

        This function handles the HTTP DELETE request to delete a state object
        from storage. The request body should not contain any data.

        Args:
            state_id (str): The id of the state object to delete.

        Returns:
            A JSON object with an empty dictionary as the response data,
            and a status code of 200 if the deletion was successful.

        Raises:
            NotFound: If the state object with the given id is not found.
    '''
    # Retrieve the state object from storage based on the given id
    state = storage.get("State", state_id)

    # If the state object is not found, return a 404 error
    if state is None:
        abort(404)

    # Delete the state object from storage
    state.delete()
    storage.save()

    # Return an empty JSON response with a status code of 200
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    '''
        Create a new state object.

        This function handles the HTTP POST request to create a new state object
        with the provided data. The request body should be a JSON object with
        the 'name' attribute.

        Returns:
            A JSON object representing the newly created state object and a
            status code of 201 if the creation was successful.

        Raises:
            BadRequest: If the request body is not a valid JSON or if the 'name'
                       attribute is missing.
    '''
    # Check if the request body is a valid JSON object
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    # Check if the 'name' attribute is provided
    elif "name" not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    else:
        # Create a new state object with the provided data
        obj_data = request.get_json()
        obj = State(**obj_data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<states_id>', methods=['PUT'], strict_slashes=False)
def update_state(states_id):
    '''
        Update an existing state object.

        This function handles the HTTP PUT request to update a state object
        identified by its id. It expects the request body to be a JSON object
        containing the new name for the state.

        Args:
            states_id (str): The id of the state object to update.

        Returns:
            A JSON object representing the updated state object and a
            status code of 200 if the update was successful.

        Raises:
            NotFound: If the state object with the given id is not found.
    '''
    # Check if the request body is a valid JSON object
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    # Retrieve the state object from storage based on the given id
    obj = storage.get("State", states_id)

    # If the state object is not found, return a 404 error
    if obj is None:
        abort(404)

    # Update the name attribute of the state object with the new name from
    # the request body
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()

    # Return the updated state object as a JSON response with a status code of
    # 200
    return jsonify(obj.to_dict()), 200
