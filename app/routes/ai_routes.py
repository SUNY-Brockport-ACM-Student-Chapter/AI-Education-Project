"""
This module contains routes and functions related to AI processing in the application.

It defines a Flask Blueprint for AI-related routes and includes functions for
AI data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.ai_model import Ai
from app.repositories.ai_repository import AIRepository
from app.services.ai_service import AiService

# Create the blueprint
ai_bp = Blueprint("ai_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
ai_repository = AIRepository(db_session)
ai_service = AiService(ai_repository)


@ai_bp.route("/ai", methods=["GET"])
def get_all_ais():
    """Get all AI assessments"""
    try:
        ais = ai_service.get_all_ais()
        return (
            jsonify(
                [
                    {
                        "ai_id": ai.ai_id,
                        "assessment_text": ai.assessment_text,
                        "grade": ai.grade,
                        "student_answer_id": ai.student_answer_id,
                    }
                    for ai in ais
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching AI assessments: {str(e)}")
        return jsonify({"error": str(e)}), 500


@ai_bp.route("/ai/<int:ai_id>", methods=["GET"])
def get_ai(ai_id):
    """Get specific AI assessment"""
    try:
        ai = ai_service.get_ai_by_id(ai_id)
        if not ai:
            return jsonify({"error": "AI assessment not found"}), 404
        return (
            jsonify(
                {
                    "ai_id": ai.ai_id,
                    "assessment_text": ai.assessment_text,
                    "grade": ai.grade,
                    "student_answer_id": ai.student_answer_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching AI assessment: {str(e)}")
        return jsonify({"error": str(e)}), 500


@ai_bp.route("/ai/process", methods=["POST"])
def process_data():
    """Create new AI assessment"""
    try:
        data = request.json
        new_ai = Ai(
            assessment_text=data.get("assessment_text"),
            student_answer_id=data.get("student_answer_id"),
            grade=data.get("grade"),
        )
        result = ai_service.create_ai(new_ai)
        return (
            jsonify(
                {
                    "ai_id": result.ai_id,
                    "assessment_text": result.assessment_text,
                    "grade": result.grade,
                    "student_answer_id": result.student_answer_id,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error during AI processing: {str(e)}")
        return jsonify({"error": str(e)}), 500


@ai_bp.route("/ai/<int:ai_id>", methods=["PUT"])
def update_ai(ai_id):
    """Update existing AI assessment"""
    try:
        data = request.json
        existing_ai = ai_service.get_ai_by_id(ai_id)
        if not existing_ai:
            return jsonify({"error": "AI assessment not found"}), 404

        existing_ai.assessment_text = data.get(
            "assessment_text", existing_ai.assessment_text
        )
        existing_ai.grade = data.get("grade", existing_ai.grade)
        existing_ai.student_answer_id = data.get(
            "student_answer_id", existing_ai.student_answer_id
        )

        updated_ai = ai_service.update_ai(existing_ai)
        return (
            jsonify(
                {
                    "ai_id": updated_ai.ai_id,
                    "assessment_text": updated_ai.assessment_text,
                    "grade": updated_ai.grade,
                    "student_answer_id": updated_ai.student_answer_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating AI assessment: {str(e)}")
        return jsonify({"error": str(e)}), 500


@ai_bp.route("/ai/<int:ai_id>", methods=["DELETE"])
def delete_ai(ai_id):
    """Delete AI assessment"""
    try:
        ai = ai_service.get_ai_by_id(ai_id)
        if not ai:
            return jsonify({"error": "AI assessment not found"}), 404

        ai_service.delete_ai(ai)
        return jsonify({"message": "AI assessment deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting AI assessment: {str(e)}")
        return jsonify({"error": str(e)}), 500
