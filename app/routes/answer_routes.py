"""
This module contains routes for the answer model (SubmissionAnswer).
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.submission_answer_repository import SubmissionAnswerRepository
from app.services.submission_answer_service import SubmissionAnswerService

# Create the blueprint
answer_bp = Blueprint("answer_bp", __name__)

# Initialize service with repository
db_session = get_db_session()

answer_repository = SubmissionAnswerRepository(db_session)

answer_service = SubmissionAnswerService(answer_repository)


# NOTE: This route is likely incomplete as it doesn't specify the student/submission.
@answer_bp.route("/create_answer/<string:question_id>", methods=["POST"]) # FIX: Changed to string
def create_answer(question_id: str): # FIX: Changed type hint
    """Create an answer for a question"""
    try:
        data = request.json
        # NOTE: Assuming 'submission_id' is also required by the service/repository but is missing here.
        # Assuming for now 'answer_text' maps to the 'response' column.
        answer_text = data.get("response") # Changed key from 'answer_text' to 'response' for consistency
        
        # NOTE: The service call likely needs `submission_id` or `user_id` context.
        # Placeholder call:
        answer = answer_service.create_answer(question_id, answer_text) 
        
        return (
            jsonify(
                {"message": "Answer created successfully", "answer": answer.to_dict()}
            ),
            201,
        )
    except ValueError as e:
        current_app.logger.error(f"Error creating answer: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error creating answer: {str(e)}")
        return jsonify({"error": "Failed to create answer"}), 500