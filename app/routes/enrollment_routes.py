"""
This module contains routes for the enrollment model.

It defines a Flask Blueprint for enrollment-related routes and includes functions for
enrollment data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.enrollment_model import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from app.services.enrollment_service import EnrollmentService

# Create the blueprint
enrollment_bp = Blueprint("enrollment_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
enrollment_repository = EnrollmentRepository(db_session)
enrollment_service = EnrollmentService(enrollment_repository)


@enrollment_bp.route("/enrollments", methods=["GET"])
def get_all_enrollments():
    """Get all enrollments"""
    try:
        enrollments = enrollment_service.get_all_enrollments()
        return (
            jsonify(
                [
                    {
                        "enrollment_id": enrollment.enrollment_id,
                        "student_id": enrollment.student_id,
                        "course_id": enrollment.course_id,
                    }
                    for enrollment in enrollments
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching enrollments: {str(e)}")
        return jsonify({"error": str(e)}), 500


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["GET"])
def get_enrollment(enrollment_id):
    """Get specific enrollment"""
    try:
        enrollment = enrollment_service.get_enrollment_by_id(enrollment_id)
        if not enrollment:
            return jsonify({"error": "Enrollment not found"}), 404
        return (
            jsonify(
                {
                    "enrollment_id": enrollment.enrollment_id,
                    "student_id": enrollment.student_id,
                    "course_id": enrollment.course_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 500


@enrollment_bp.route("/enrollments", methods=["POST"])
def create_enrollment():
    """Create a new enrollment"""
    try:
        data = request.json
        new_enrollment = Enrollment(
            student_id=data.get("student_id"), course_id=data.get("course_id")
        )
        result = enrollment_service.create_enrollment(new_enrollment)
        return (
            jsonify(
                {
                    "enrollment_id": result.enrollment_id,
                    "student_id": result.student_id,
                    "course_id": result.course_id,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 500


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["PUT"])
def update_enrollment(enrollment_id):
    """Update existing enrollment"""
    try:
        data = request.json
        existing_enrollment = enrollment_service.get_enrollment_by_id(enrollment_id)
        if not existing_enrollment:
            return jsonify({"error": "Enrollment not found"}), 404

        existing_enrollment.student_id = data.get(
            "student_id", existing_enrollment.student_id
        )
        existing_enrollment.course_id = data.get(
            "course_id", existing_enrollment.course_id
        )

        updated_enrollment = enrollment_service.update_enrollment(existing_enrollment)
        return (
            jsonify(
                {
                    "enrollment_id": updated_enrollment.enrollment_id,
                    "student_id": updated_enrollment.student_id,
                    "course_id": updated_enrollment.course_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 500


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["DELETE"])
def delete_enrollment(enrollment_id):
    """Delete existing enrollment"""
    try:
        enrollment = enrollment_service.get_enrollment_by_id(enrollment_id)
        if not enrollment:
            return jsonify({"error": "Enrollment not found"}), 404

        enrollment_service.delete_enrollment(enrollment)
        return jsonify({"message": "Enrollment deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 500
