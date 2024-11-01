"""
This module contains routes for the answer model. 
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.answer_model import Answer
from app.repositories.answer_repository import AnswerRepository
from app.services.answer_service import AnswerService

# Create the blueprint
answer_bp = Blueprint("answer_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
answer_repository = AnswerRepository(db_session)
answer_service = AnswerService(answer_repository)


@answer_bp.route("/answers", methods=["GET"])
def get_all_answers():
    """Get all answers"""
    try:
        answers = answer_service.get_all_answers()
        return (
            jsonify(
                [
                    {
                        "answer_id": answer.answer_id,
                        "answer_text": answer.answer_text,
                        "question_id": answer.question_id,
                    }
                    for answer in answers
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching answers: {str(e)}")
        return jsonify({"error": str(e)}), 500


@answer_bp.route("/answers/<int:answer_id>", methods=["GET"])
def get_answer(answer_id):
    """Get specific answer"""
    try:
        answer = answer_service.get_answer_by_id(answer_id)
        if not answer:
            return jsonify({"error": "Answer not found"}), 404
        return (
            jsonify(
                {
                    "answer_id": answer.answer_id,
                    "answer_text": answer.answer_text,
                    "student_id": answer.student_id,
                    "question_id": answer.question_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@answer_bp.route("/answers", methods=["POST"])
def create_answer():
    """Create a new answer"""
    try:
        data = request.json
        new_answer = Answer(
            answer_text=data.get("answer_text"),
            student_id=data.get("student_id"),
            question_id=data.get("question_id"),
        )
        result = answer_service.create_answer(new_answer)
        return (
            jsonify(
                {
                    "answer_id": result.answer_id,
                    "answer_text": result.answer_text,
                    "student_id": result.student_id,
                    "question_id": result.question_id,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@answer_bp.route("/answers/<int:answer_id>", methods=["PUT"])
def update_answer(answer_id):
    """Update existing answer"""
    try:
        data = request.json
        existing_answer = answer_service.get_answer_by_id(answer_id)
        if not existing_answer:
            return jsonify({"error": "Answer not found"}), 404

        existing_answer.answer_text = data.get(
            "answer_text", existing_answer.answer_text
        )
        existing_answer.student_id = data.get("student_id", existing_answer.student_id)
        existing_answer.question_id = data.get(
            "question_id", existing_answer.question_id
        )

        updated_answer = answer_service.update_answer(existing_answer)
        return (
            jsonify(
                {
                    "answer_id": updated_answer.answer_id,
                    "answer_text": updated_answer.answer_text,
                    "student_id": updated_answer.student_id,
                    "question_id": updated_answer.question_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@answer_bp.route("/answers/<int:answer_id>", methods=["DELETE"])
def delete_answer(answer_id):
    """Delete existing answer"""
    try:
        answer = answer_service.get_answer_by_id(answer_id)
        if not answer:
            return jsonify({"error": "Answer not found"}), 404

        answer_service.delete_answer(answer)
        return jsonify({"message": "Answer deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting answer: {str(e)}")
        return jsonify({"error": str(e)}), 500
