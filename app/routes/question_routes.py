"""
This module contains routes for the question model.

It defines a Flask Blueprint for question-related routes and includes functions for
question data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from database import get_db_session
from models.question_model import Question
from repositories.question_repository import QuestionRepository
from services.question_service import QuestionService

# Create the blueprint
question_bp = Blueprint("question_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
question_repository = QuestionRepository(db_session)
question_service = QuestionService(question_repository)


@question_bp.route("/questions", methods=["GET"])
def get_all_questions():
    """Get all questions"""
    try:
        questions = question_service.get_all_questions()
        return (
            jsonify(
                [
                    {
                        "question_id": question.question_id,
                        "question_text": question.question_text,
                        "exam_id": question.exam_id,
                    }
                    for question in questions
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching questions: {str(e)}")
        return jsonify({"error": str(e)}), 500


@question_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    """Get specific question"""
    try:
        question = question_service.get_question_by_id(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404
        return (
            jsonify(
                {
                    "question_id": question.question_id,
                    "question_text": question.question_text,
                    "exam_id": question.exam_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching question: {str(e)}")
        return jsonify({"error": str(e)}), 500


@question_bp.route("/questions", methods=["POST"])
def create_question():
    """Create a new question"""
    try:
        data = request.json
        new_question = Question(
            question_text=data.get("question_text"), exam_id=data.get("exam_id")
        )
        result = question_service.create_question(new_question)
        return (
            jsonify(
                {
                    "question_id": result.question_id,
                    "question_text": result.question_text,
                    "exam_id": result.exam_id,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating question: {str(e)}")
        return jsonify({"error": str(e)}), 500


@question_bp.route("/questions/<int:question_id>", methods=["PUT"])
def update_question(question_id):
    """Update existing question"""
    try:
        data = request.json
        existing_question = question_service.get_question_by_id(question_id)
        if not existing_question:
            return jsonify({"error": "Question not found"}), 404

        existing_question.question_text = data.get(
            "question_text", existing_question.question_text
        )
        existing_question.exam_id = data.get("exam_id", existing_question.exam_id)

        updated_question = question_service.update_question(existing_question)
        return (
            jsonify(
                {
                    "question_id": updated_question.question_id,
                    "question_text": updated_question.question_text,
                    "exam_id": updated_question.exam_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating question: {str(e)}")
        return jsonify({"error": str(e)}), 500


@question_bp.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    """Delete existing question"""
    try:
        question = question_service.get_question_by_id(question_id)
        if not question:
            return jsonify({"error": "Question not found"}), 404

        question_service.delete_question(question)
        return jsonify({"message": "Question deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting question: {str(e)}")
        return jsonify({"error": str(e)}), 500
