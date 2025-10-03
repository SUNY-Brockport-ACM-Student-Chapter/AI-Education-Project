"""
This module contains routes and functions related to AI processing in the application.

It defines a Flask Blueprint for AI-related routes and includes functions for
AI data processing.
"""

from flask import Blueprint, current_app, jsonify

from app.database import get_db_session
from app.repositories.ai_interaction_repository import AiInteractionRepository
# SubmissionAnswerRepository is not strictly needed in routes
from app.services.ai_interaction_service import AiInteractionService # Correct Service
# SubmissionAnswerService is not needed for AI feedback retrieval here

# Create the blueprint
ai_bp = Blueprint("ai_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
ai_repository = AiInteractionRepository(db_session)
# FIX: Initialize with the correct service (AiInteractionService)
ai_service = AiInteractionService(ai_repository) 


@ai_bp.route(
    # FIX: Use 'submission_id' and 'string' type (assuming UUID)
    "/get_ai_assessment_for_submission/<string:submission_id>", methods=["GET"]
)
# FIX: Renamed function and parameter to align with repository logic (submission_id, assessment)
def get_ai_assessment_for_submission(submission_id: str): 
    """Get AI assessment for a submission"""
    try:
        # FIX: Renamed service method 
        ai_interaction = ai_service.get_ai_assessment_for_submission(submission_id) 

        if not ai_interaction: # FIX: Renamed variable
            # FIX: Corrected typo in message
            return jsonify({"error": "No AI assessment found for this submission"}), 404

        return jsonify(ai_interaction.to_dict()), 200 # FIX: Renamed variable
    except ValueError as e:
        current_app.logger.error(
            f"Error fetching AI assessment for submission: {str(e)}"
        )
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(
            f"Error fetching AI assessment for submission: {str(e)}"
        )
        return jsonify({"error": "Internal server error during AI assessment fetch"}), 500