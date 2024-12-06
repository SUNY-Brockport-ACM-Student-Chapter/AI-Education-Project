"""
This module contains the routes for the teacher.

It defines a Flask Blueprint for the teacher routes and includes functions for
handling the teacher routes.
"""

from flask import Blueprint, current_app, jsonify

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


@teacher_bp.route("/get_teacher_by_id/<int:teacher_id>", methods=["GET"])
def get_teacher_by_id(teacher_id: int):
    """Get a teacher by their ID"""
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        return jsonify({"teacher": teacher.to_dict()}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error fetching teacher by ID: {str(e)}")
        return jsonify({"error": "Failed to fetch teacher by ID"}), 500


