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


@student_bp.route("/students", methods=["GET"])
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


@student_bp.route("/students/<int:student_id>", methods=["GET"])
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
                    "student_name": student.first_name + " " + student.last_name
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/students", methods=["POST"])
def create_student():
    """Create a new student"""
    try:
        data = request.json
        new_student = Student(student_name=data.get("student_name"))
        result = student_service.create_student(new_student)
        return (
            jsonify(
                {
                    "student_id": result.student_id, 
                    "student_name": result.first_name + " " + result.last_name
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update existing student"""
    try:
        data = request.json
        existing_student = student_service.get_student_by_id(student_id)
        if not existing_student:
            return jsonify({"error": "Student not found"}), 404

        existing_student.student_name = data.get(
            "student_name", existing_student.student_name
        )

        updated_student = student_service.update_student(existing_student)
        return (
            jsonify(
                {
                    "student_id": updated_student.student_id,
                    "student_name": updated_student.student_name,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating student: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
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
