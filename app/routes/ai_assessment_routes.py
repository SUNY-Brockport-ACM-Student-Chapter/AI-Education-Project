"""
This module contains routes and functions related to AI processing in the application.

It defines a Flask Blueprint for AI-related routes and includes functions for
AI data processing.
"""

from flask import Blueprint, current_app, jsonify

from app.database import get_db_session
from app.repositories.ai_assessment_repository import AiAssessmentRepository
from app.repositories.studentAnswer_repository import StudentAnswerRepository
from app.services.ai_assessment_service import AiAssessmentService
from app.services.studentAnswer_service import StudentAnswerService

# Create the blueprint
ai_bp = Blueprint("ai_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
ai_repository = AiAssessmentRepository(db_session)
ai_service = AiAssessmentService(ai_repository)


@ai_bp.route(
    "/get_ai_assesment_for_studentAnswer/<int:studentAnswer_id>", methods=["GET"]
)
def get_ai_assesment_for_studentAnswer(studentAnswer_id: int):
    """Get AI assesment for a student answer"""
    try:
        ai = ai_service.get_ai_assesment_for_studentAnswer(studentAnswer_id)

        if not ai:
            return jsonify({"error": "No AI assesments found"}), 404

        return jsonify(ai.to_dict()), 200
    except ValueError as e:
        current_app.logger.error(
            f"Error fetching AI assesment for student answer: {str(e)}"
        )
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(
            f"Error fetching AI assesment for student answer: {str(e)}"
        )
        return jsonify({"error": str(e)}), 500
