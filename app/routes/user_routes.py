"""
This module contains routes and functions related to user management in the application.

It defines a Flask Blueprint for user-related routes and includes functions for
handling user operations such as registration.
"""

from flask import Blueprint, request, jsonify, current_app
from ..models import Teacher, db
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user.
    

    This route handles POST requests to register a new user. It expects JSON data
    containing 'username', 'password_hash', and 'role' fields.

    Returns:
        flask.Response: A JSON response indicating successful user registration.
    """
    try:
        data = request.json
        if not all(k in data for k in ("username", "password", "role")):
            current_app.logger.warning('Registration attempt with missing fields')
            return jsonify({'error': 'Missing required fields'}), 400
        if data['role'] not in ['student', 'teacher']:
            current_app.logger.warning(f'Registration attempt with invalid role: {data["role"]}')
            return jsonify({'error': 'Invalid role'}), 400
        
        new_user = Teacher(
            username=data['username'],
            password_hash=generate_password_hash(data['password']),
            role=data['role']
        )
        db.session.add(new_user)
        db.session.commit()
        current_app.logger.info(f'New user registered: {new_user.username}')
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f'Error during user registration: {str(e)}')
        return jsonify({'error': str(e)}), 500