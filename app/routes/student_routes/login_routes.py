from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timezone

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

student_auth_bp = Blueprint("student_auth_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)

@student_auth_bp.route("/login", methods=["POST"])
def login():
    """Student login endpoint"""
    try:
        data = request.json
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({"error": "Missing username or password"}), 400

        # Add method to repository and service
        student = student_service.get_student_by_username(data['username'])
        
        if not student:
            return jsonify({"error": "Invalid username or password"}), 401
        
        if not student.check_password(data['password']):
            return jsonify({"error": "Invalid username or password"}), 401

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
