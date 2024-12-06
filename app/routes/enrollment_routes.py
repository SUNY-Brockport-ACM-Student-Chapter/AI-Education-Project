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




@enrollment_bp.route("/change_enrollment_status_for_student/<int:student_id>/<int:course_id>", methods=["PUT"])
def change_enrollment_status_for_student(student_id, course_id):
    """Change the enrollment status for a student"""
    try:
        data = request.get_json()
        status = data.get("status")
        enrollment = enrollment_service.change_enrollment_status_for_student(student_id, course_id, status)
        return jsonify({"enrollment": enrollment.to_dict(), "message": "Enrollment status changed successfully"}), 200
    except ValueError as e:
        current_app.logger.error(f"Error changing enrollment status for student: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error changing enrollment status for student: {str(e)}")
        return jsonify({"error": "Failed to change enrollment status for student"}), 500


@enrollment_bp.route("/create_enrollment/<int:student_id>/<int:course_id>", methods=["POST"])
def create_enrollment(student_id, course_id):
    """Create an enrollment for a student"""
    try:
        enrollment = enrollment_service.create_enrollment(student_id, course_id)
        return jsonify({"enrollment": enrollment.to_dict(), "message": "Enrollment created successfully"}), 200
    except ValueError as e:
        current_app.logger.error(f"Error creating enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error creating enrollment: {str(e)}")
        return jsonify({"error": "Failed to create enrollment"}), 500

