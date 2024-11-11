"""
This module contains the routes for the teacher.

It defines a Flask Blueprint for the teacher routes and includes functions for
handling the teacher routes.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.teacher_model import Teacher
from app.repositories.teacher_repository import TeacherRepository
from app.services.teacher_service import TeacherService

# Create the blueprint
teacher_bp = Blueprint("teacher_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
teacher_repository = TeacherRepository(db_session)
teacher_service = TeacherService(teacher_repository)


@teacher_bp.route("/teachers", methods=["GET"])
def get_all_teachers():
    """Get all teachers"""
    try:
        teachers = teacher_service.get_all_teachers()
        return (
            jsonify(
                [
                    {
                        "teacher_id": teacher.teacher_id,
                        "first_name": teacher.first_name,
                        "last_name": teacher.last_name,
                        "email": teacher.email,
                    }
                    for teacher in teachers
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching teachers: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    """Get specific teacher"""
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not teacher:
            return jsonify({"error": "Teacher not found"}), 404
        return (
            jsonify(
                {"teacher_id": teacher.teacher_id, "teacher_name": teacher.teacher_name}
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/teachers", methods=["POST"])
def create_teacher():
    """Create a new teacher"""
    try:
        data = request.json
        new_teacher = Teacher(teacher_name=data.get("teacher_name"))
        result = teacher_service.create_teacher(new_teacher)
        return (
            jsonify(
                {"teacher_id": result.teacher_id, "teacher_name": result.teacher_name}
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["PUT"])
def update_teacher(teacher_id):
    """Update existing teacher"""
    try:
        data = request.json
        existing_teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not existing_teacher:
            return jsonify({"error": "Teacher not found"}), 404

        existing_teacher.teacher_name = data.get(
            "teacher_name", existing_teacher.teacher_name
        )

        updated_teacher = teacher_service.update_teacher(existing_teacher)
        return (
            jsonify(
                {
                    "teacher_id": updated_teacher.teacher_id,
                    "teacher_name": updated_teacher.teacher_name,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["DELETE"])
def delete_teacher(teacher_id):
    """Delete existing teacher"""
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not teacher:
            return jsonify({"error": "Teacher not found"}), 404

        teacher_service.delete_teacher(teacher)
        return jsonify({"message": "Teacher deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500
