"""
This module contains routes and functions related to user management in the application.

It defines a Flask Blueprint for user-related routes and includes functions for
handling user operations such as registration.
"""

from flask import Blueprint, current_app, jsonify, request
from werkzeug.security import generate_password_hash

from app.database import get_db_session
from app.models.teacher_model import Teacher
from app.repositories.teacher_repository import TeacherRepository
from app.services.teacher_service import TeacherService

user_bp = Blueprint("user_bp", __name__)

# Initialize services
db_session = get_db_session()
teacher_repository = TeacherRepository(db_session)
teacher_service = TeacherService(teacher_repository)


@user_bp.route("/register", methods=["POST"])
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
            current_app.logger.warning("Registration attempt with missing fields")
            return jsonify({"error": "Missing required fields"}), 400
        if data["role"] not in ["student", "teacher"]:
            current_app.logger.warning(
                f'Registration attempt with invalid role: {data["role"]}'
            )
            return jsonify({"error": "Invalid role"}), 400

        new_user = Teacher(
            username=data["username"],
            password_hash=generate_password_hash(data["password"]),
            role=data["role"],
        )
        db_session.add(new_user)
        db_session.commit()
        current_app.logger.info(f"New user registered: {new_user.username}")
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        db_session.rollback()
        current_app.logger.error(f"Error during user registration: {str(e)}")
        return jsonify({"error": str(e)}), 500
