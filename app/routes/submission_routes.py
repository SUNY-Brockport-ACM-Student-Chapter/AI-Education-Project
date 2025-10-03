"""
This module contains routes for the Submission model, following the /submission RESTful pattern.
This resource tracks the overall attempt/status for an assignment by a student.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
# Assuming repository and service exist for Submission
from app.repositories.submission_repository import SubmissionRepository
from app.services.submission_service import SubmissionService

# Create the blueprint with RESTful prefix
submission_bp = Blueprint("submission_bp", __name__)

# Initialize service with repository (MOCK for now)
db_session = get_db_session()
submission_repository = SubmissionRepository(db_session)
submission_service = SubmissionService(submission_repository)


@submission_bp.route("/submission", methods=["POST"])
def create_submission():
    """POST /submission: Create a new submission (start of an attempt)."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400
            
        submission = submission_service.create_submission(data)
        
        return jsonify({"id": submission.id, "message": "Submission created successfully"}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating submission: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating submission: {str(e)}")
        return jsonify({"error": "Failed to create submission"}), 500


@submission_bp.route("/submission/<string:submission_id>", methods=["GET", "PATCH", "DELETE"])
def handle_submission(submission_id: str):
    """Handle GET, PATCH, and DELETE operations for a single Submission."""
    try:
        if request.method == "GET":
            submission = submission_service.get_submission_by_id(submission_id)
            if not submission:
                return jsonify({"error": "Submission not found"}), 404
            return jsonify(submission.to_dict()), 200

        elif request.method == "PATCH":
            data = request.json
            if not data:
                return jsonify({"error": "Missing JSON data for update"}), 400

            submission = submission_service.update_submission(submission_id, data)
            return jsonify(submission.to_dict()), 200

        elif request.method == "DELETE":
            submission_service.delete_submission(submission_id)
            return "", 204
    
    except ValueError as e:
        current_app.logger.error(f"Error handling submission {submission_id}: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error handling submission: {str(e)}")
        return jsonify({"error": "Failed to process submission request"}), 500
