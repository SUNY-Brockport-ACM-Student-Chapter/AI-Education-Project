""" 
This module contains routes for the student model.
 
It defines a Flask Blueprint for the student routes and includes functions for
handling the student routes.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

# Create the blueprint
student_bp = Blueprint("student_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)


@student_bp.route("/get_all_students", methods=["GET"])
def get_all_students():
    """Get all students"""
    try:
        students = student_service.get_all_students()
        return (
            jsonify(
                [
                    {
                        "student_id": student.student_id,
                        "student_name": student.first_name + " " + student.last_name,
                    }
                    for student in students
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching students: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/get_student_by_id/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Get specific student"""
    try:
        student = student_service.get_student_by_id(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404
        return (
            jsonify(
                {
                    "student_id": student.student_id,
                    "student_name": student.first_name + " " + student.last_name,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/create_student", methods=["POST"])
def create_student():
    """Create a new student"""
    try:
        data = request.json
        new_student = Student(
            clerk_user_id=data.get("clerk_user_id"),
            user_name=data.get("user_name"),
            email=data.get("email"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
            )
        result = student_service.create_student(new_student)
        return (
            jsonify(
                {
                    "student_id": result.student_id,
                    "student_name": result.first_name + " " + result.last_name,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/update_student_by_id/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update existing student"""
    try:
        data = request.json
        existing_student = student_service.get_student_by_id(student_id)
        if not existing_student:
            return jsonify({"error": "Student not found"}), 404

        # Update only the attributes that are provided in the request
        # Partial updates
        if "clerk_user_id" in data:
            existing_student.clerk_user_id = data["clerk_user_id"]
        if "user_name" in data:
            existing_student.user_name = data["user_name"]
        if "email" in data:
            existing_student.email = data["email"]
        if "first_name" in data:
            existing_student.first_name = data["first_name"]
        if "last_name" in data:
            existing_student.last_name = data["last_name"]
        if "is_active" in data:
            existing_student.is_active = data["is_active"]
        if "last_login" in data:
            existing_student.last_login = data["last_login"]

        # Update the student in the database
        updated_student = student_service.update_student(existing_student)

        return (
            jsonify(
                {
                    "student_id": updated_student.student_id,
                    "user_name": updated_student.user_name,
                    "email": updated_student.email,
                    "first_name": updated_student.first_name,
                    "last_name": updated_student.last_name,
                    "is_active": updated_student.is_active,
                    "last_login": updated_student.last_login.isoformat() if updated_student.last_login else None,
                    "created_at": updated_student.created_at.isoformat() if updated_student.created_at else None,
                    "updated_at": updated_student.updated_at.isoformat() if updated_student.updated_at else None,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/delete_student_by_id/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete existing student"""
    try:
        student = student_service.get_student_by_id(student_id)
        if not student:
            return jsonify({"error": "Student not found"}), 404

        student_service.delete_student(student)
        return jsonify({"message": "Student deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting student: {str(e)}")
        return jsonify({"error": str(e)}), 500
