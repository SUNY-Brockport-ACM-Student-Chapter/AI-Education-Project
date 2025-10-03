"""
This module contains the routes for the User model, following the /user RESTful pattern.
"""
from flask import Blueprint, request, jsonify, current_app

from app.database import get_db_session
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


user_repo = UserRepository(get_db_session())
user_service = UserService(user_repo) # Replace with real service initialization
user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/user', methods=['POST'])
def create_user():
    """POST /user: Creates a new user."""
    try:
        user_data = request.get_json()
        if not user_data:
            return jsonify({"error": "Missing JSON data"}), 400
        
        # Call service to create user
        user = user_service.create_user(user_data)
        
        # Response should be the ID of the new resource
        return jsonify({"id": user.id}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating user: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating user: {str(e)}")
        return jsonify({"error": "Failed to create user"}), 500

@user_bp.route('/user/<string:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_user(user_id: str):
    """Handle GET, PATCH, and DELETE operations for a single user."""
    # try:
    if request.method == 'GET':
        user = user_service.get_user_by_id(user_id)
        
        if user is None:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404
        
        return jsonify(user.to_dict()), 200

    elif request.method == 'PATCH':
        update_data = request.get_json()
        if not update_data:
            return jsonify({"error": "Missing JSON data"}), 400

        # Call service to update user
        updated_user = user_service.update_user(user_id, update_data)
        
        if updated_user is None:
            return jsonify({"error": f"User with ID {user_id} not found"}), 404
            
        # Return 200 OK with the updated resource
        return jsonify(updated_user.to_dict()), 200

    elif request.method == 'DELETE':
        # Call service to delete user
        success = user_service.delete_user(user_id)
        if not success:
                return jsonify({"error": f"User with ID {user_id} not found or could not be deleted"}), 404
                
        # Return 204 No Content
        return '', 204
    
    # except ValueError as e:
    #     current_app.logger.error(f"Error handling user {user_id}: {str(e)}")
    #     return jsonify({"error": str(e)}), 404
    # except Exception as e:
    #     current_app.logger.error(f"Internal error handling user: {str(e)}")
    #     return jsonify({"error": "Failed to process user request"}), 500
