"""
This module contains routes for the enrollment model, following the /enrollment RESTful pattern.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.enrollment_repository import EnrollmentRepository
from app.services.enrollment_service import EnrollmentService

# Create the blueprint with RESTful prefix
enrollment_bp = Blueprint("enrollment_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
enrollment_repository = EnrollmentRepository(db_session)
enrollment_service = EnrollmentService(enrollment_repository)


@enrollment_bp.route("/enrollment", methods=["POST"])
def create_enrollment():
    """POST /enrollment: Create a new enrollment (student into course)."""
    try:
        data = request.get_json()
        if not data or not data.get("student_id") or not data.get("course_id"):
            return jsonify({"error": "Missing 'student_id' or 'course_id' in JSON data"}), 400
            
        student_id = data["student_id"]
        course_id = data["course_id"]
        
        enrollment = enrollment_service.create_enrollment(student_id, course_id)
        return jsonify({"id": enrollment.id, "message": "Enrollment created successfully"}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating enrollment: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating enrollment: {str(e)}")
        return jsonify({"error": "Failed to create enrollment"}), 500


# Endpoint to handle status changes (PUT is appropriate for full resource state replacement/update)
@enrollment_bp.route("/enrollment/status/<string:student_id>/<string:course_id>", methods=["PUT"])
def change_enrollment_status(student_id: str, course_id: str):
    """PUT /enrollment/status/{student_id}/{course_id}: Change the enrollment status."""
    try:
        data = request.get_json()
        status = data.get("status")
        if not status:
            return jsonify({"error": "Missing 'status' field in JSON data"}), 400
            
        enrollment = enrollment_service.change_enrollment_status_for_student(
            student_id, course_id, status
        )
        return (
            jsonify(
                {
                    "enrollment": enrollment.to_dict(),
                    "message": "Enrollment status changed successfully",
                }
            ),
            200,
        )
    except ValueError as e:
        current_app.logger.error(f"Error changing enrollment status: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error changing enrollment status: {str(e)}")
        return jsonify({"error": "Failed to change enrollment status"}), 500


# Assuming an enrollment ID exists for single GET/PATCH/DELETE
@enrollment_bp.route("/enrollment/<string:enrollment_id>", methods=["GET", "PATCH", "DELETE"])
def handle_enrollment(enrollment_id: str):
    """Handle GET, PATCH, and DELETE operations for a single Enrollment."""
    try:
        if request.method == "GET":
            enrollment = enrollment_service.get_enrollment_by_id(enrollment_id)
            if not enrollment:
                return jsonify({"error": "Enrollment not found"}), 404
            return jsonify(enrollment.to_dict()), 200

        elif request.method == "PATCH":
            data = request.json
            if not data:
                return jsonify({"error": "Missing JSON data for update"}), 400

            enrollment = enrollment_service.update_enrollment(enrollment_id, data)
            return jsonify(enrollment.to_dict()), 200

        elif request.method == "DELETE":
            enrollment_service.delete_enrollment(enrollment_id)
            return "", 204
    
    except ValueError as e:
        current_app.logger.error(f"Error handling enrollment {enrollment_id}: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error handling enrollment: {str(e)}")
        return jsonify({"error": "Failed to process enrollment request"}), 500
