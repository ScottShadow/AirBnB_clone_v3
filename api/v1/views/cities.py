#!/usr/bin/python3
'''
    RESTful API for City class
'''
from flask import Flask, jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_city_by_state(state_id):
    '''
        Get all cities in a state

        Returns a JSON object of cities in the state.

        Args:
            state_id (str): The id of the state

        Returns:
            Tuple:
                JSON object of cities in the state
                HTTP status code 200

        Raises:
            404: If the state does not exist
    '''
    # Get state object from storage
    state = storage.get("State", state_id)
    # If state object does not exist, return 404
    if state is None:
        abort(404)
    # Convert list of city objects to list of dictionaries
    city_list = [c.to_dict() for c in state.cities]
    # Return list of city dictionaries as JSON object
    return jsonify(city_list), 200
    return jsonify(city_list), 200


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city_id(city_id):
    '''
        Retrieve city by its id and return it as a JSON object.

        Args:
            city_id (str): The id of the city to retrieve.

        Returns:
            Tuple:
                JSON object representing the city.
                HTTP status code 200.

        Raises:
            404: If the city does not exist.
    '''
    # Retrieve city object from storage.
    city = storage.get("City", city_id)

    # If city object does not exist, return 404.
    if city is None:
        abort(404)

    # Return city dictionary as JSON object.
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    '''
        DELETE city obj given city_id

        Args:
            city_id (str): The id of the city to delete.

        Returns:
            Tuple:
                Empty JSON object.
                HTTP status code 200.

        Raises:
            404: If the city does not exist.
    '''
    # Retrieve city object from storage.
    city = storage.get("City", city_id)

    # If city object does not exist, return 404.
    if city is None:
        abort(404)

    # Delete city object from storage.
    city.delete()

    # Save changes to storage.
    storage.save()

    # Return empty JSON object and HTTP status code 200.
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    '''
        Create a new city object through the state association using POST.

        Args:
            state_id (str): The id of the state.

        Returns:
            Tuple:
                JSON object representing the created city.
                HTTP status code 201.

        Raises:
            400: If the request is not a JSON or if name field is missing.
            404: If the state with the given state_id does not exist.
    '''
    # Check if the request is a JSON and if it contains the 'name' field.
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in request.get_json():
        return jsonify({"error": "Missing name"}), 400
    else:
        # Get the JSON data from the request.
        obj_data = request.get_json()

        # Retrieve the state object from storage using the state_id.
        state = storage.get("State", state_id)

        # If the state object does not exist, return a 404 error.
        if state is None:
            abort(404)

        # Add the state_id to the object data.
        obj_data['state_id'] = state.id

        # Create a new City object with the object data.
        obj = City(**obj_data)

        # Save the new city object to storage.
        obj.save()

        # Return the city object as a JSON object with HTTP status code 201.
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    '''
        Update an existing city object.

        This function handles the HTTP PUT request to update a city object
        identified by its id. It expects the request body to be a JSON object
        containing the new name for the city.

        Args:
            city_id (str): The id of the city object to update.

        Returns:
            A JSON object representing the updated city object and a
            status code of 200 if the update was successful.

        Raises:
            NotFound: If the city object with the given id is not found.
    '''
    # Check if the request body is a valid JSON object
    if not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400

    # Retrieve the city object from storage based on the given id
    obj = storage.get("City", city_id)

    # If the city object is not found, return a 404 error
    if obj is None:
        abort(404)

    # Update the name attribute of the city object with the new name from
    # the request body
    obj_data = request.get_json()
    obj.name = obj_data['name']
    obj.save()

    # Return the updated city object as a JSON response with a status code of
    # 200
    return jsonify(obj.to_dict()), 200
