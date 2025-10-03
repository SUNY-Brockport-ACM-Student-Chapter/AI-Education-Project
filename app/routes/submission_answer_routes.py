"""
This module contains the routes for individual SubmissionAnswer records,
following the /submission_answer RESTful pattern.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.submission_answer_repository import SubmissionAnswerRepository
from app.services.submission_answer_service import SubmissionAnswerService

# Create the blueprint with RESTful prefix
submission_answer_bp = Blueprint("submission_answer_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
submission_answer_repository = SubmissionAnswerRepository(db_session)
submission_answer_service = SubmissionAnswerService(submission_answer_repository)


@submission_answer_bp.route("/submission_answer", methods=["POST"])
def create_submission_answer():
    """Create a new SubmissionAnswer."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400
            
        submission_answer = submission_answer_service.create_submission_answer(data)
        
        return jsonify({"id": submission_answer.id, "message": "Submission Answer created successfully"}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating submission answer: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating submission answer: {str(e)}")
        return jsonify({"error": "Failed to create submission answer"}), 500


@submission_answer_bp.route("/submission_answer/<string:answer_id>", methods=["GET", "PATCH", "DELETE"])
def handle_submission_answer(answer_id: str):
    """Handle GET, PATCH, and DELETE operations for a single SubmissionAnswer."""
    try:
        if request.method == "GET":
            submission_answer = submission_answer_service.get_submission_answer(answer_id)
            if not submission_answer:
                return jsonify({"error": "Submission Answer not found"}), 404
            return jsonify(submission_answer.to_dict()), 200

        elif request.method == "PATCH":
            data = request.json
            if not data:
                return jsonify({"error": "Missing JSON data for update"}), 400
                
            submission_answer = submission_answer_service.update_submission_answer(answer_id, data)
            return jsonify(submission_answer.to_dict()), 200

        elif request.method == "DELETE":
            submission_answer_service.delete_submission_answer(answer_id)
            return "", 204
    
    except ValueError as e:
        current_app.logger.error(f"Error handling submission answer {answer_id}: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error handling submission answer: {str(e)}")
        return jsonify({"error": "Failed to process submission answer request"}), 500


# Collection filter route: Get all answers for a specific student and question combination
@submission_answer_bp.route("/", methods=["GET"])
def get_submission_answers_filtered():
    """Get submission answers filtered by student_id and/or question_id via query params."""
    try:
        student_id = request.args.get("student_id")
        question_id = request.args.get("question_id")

        if not student_id and not question_id:
             # If no filters are provided, this implies listing all, which may be too broad.
             # You might require at least one filter or implement proper pagination for a full list route.
             return jsonify({"error": "Missing required query parameters (student_id or question_id)"}), 400

        # Assuming service method handles filtering based on provided optional parameters
        student_answers = submission_answer_service.get_submission_answers_filtered(
            student_id, question_id
        )
        student_answers_dict = [
            student_answer.to_dict() for student_answer in student_answers
        ]
        return jsonify({"submission_answers": student_answers_dict}), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error fetching submission answers: {str(e)}")
        return jsonify({"error": "Failed to fetch submission answers"}), 500
