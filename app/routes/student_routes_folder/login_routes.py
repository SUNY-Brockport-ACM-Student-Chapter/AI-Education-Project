from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timezone
from clerk_backend_api import Clerk
import os
import jwt

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

student_auth_bp = Blueprint("student_auth_bp", __name__)

# Initialize Clerk
clerk = Clerk(os.getenv('CLERK_SECRET_KEY'))

# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)

@student_auth_bp.route("/login", methods=["POST"])
def login():
    """Student login endpoint with JWT verification"""
    try:
        # Get the JWT from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "No JWT provided"}), 401

        token = auth_header.split(' ')[1]

        try:
            # Verify the JWT token
            decoded_token = jwt.decode(token, os.getenv('CLERK_JWT_SECRET'), algorithms=["HS256"])
            clerk_user_id = decoded_token['sub']  # Get the Clerk user ID from token
        except jwt.InvalidTokenError as e:
            current_app.logger.error(f"JWT verification failed: {str(e)}")
            return jsonify({"error": "Invalid JWT token"}), 401

        # Get student by Clerk user ID and verify stored JWT matches
        student = student_service.get_student_by_clerk_id(clerk_user_id)
        if not student or student.clerk_user_id != clerk_user_id:
            return jsonify({"error": "Unauthorized access"}), 401

        # Update last login time
        student.last_login = datetime.now(timezone.utc)
        student_service.update_student(student)

        return jsonify({
            "message": "Login successful",
            "student": {
                "student_id": student.student_id,
                "username": student.user_name,
                "email": student.email,
                "first_name": student.first_name,
                "last_name": student.last_name
            }
        }), 200

    except Exception as e:
        current_app.logger.error(f"Login error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@student_auth_bp.route("/register", methods=["POST"])
def register():
    """Register new student with Clerk"""
    try:
        data = request.json
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        # Create user in Clerk
        try:
            clerk_user = clerk.users.create(
                email_address=[{"email": email}],
                password=password
            )
            clerk_user_id = clerk_user['id']
        except Exception as e:
            current_app.logger.error(f"Clerk user creation failed: {str(e)}")
            return jsonify({"error": "Failed to create user"}), 400

        # Create student in database
        new_student = Student(
            email=email,
            clerk_user_id=clerk_user_id,
            user_name=email,  # You might want to generate a username differently
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        student_service.create_student(new_student)

        return jsonify({"message": "Student registered successfully"}), 201

    except Exception as e:
        current_app.logger.error(f"Registration error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
