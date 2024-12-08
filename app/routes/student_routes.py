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


@student_bp.route("/search_for_students", methods=["GET"])
def search_for_students():
    """Search for students"""
    try:
        students = student_service.search_for_students(request.json)
        students_dict = [student.to_dict() for student in students]
        return jsonify({"students": students_dict}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error searching for students: {str(e)}")
        return jsonify({"error": "Failed to search for students"}), 500


@student_bp.route("/get_students_for_course/<int:course_id>", methods=["GET"])
def get_students_for_course(course_id: int):
    """Get students for a course"""
    try:
        students = student_service.get_students_for_course(course_id)
        students_dict = [student.to_dict() for student in students]
        return jsonify({"students": students_dict}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching students for course: {str(e)}")
        return jsonify({"error": "Failed to fetch students for course"}), 500
