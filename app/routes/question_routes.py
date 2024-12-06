"""
This module contains routes for the question model.

It defines a Flask Blueprint for question-related routes and includes functions for
question data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.question_model import Question
from app.repositories.question_repository import QuestionRepository
from app.services.question_service import QuestionService

# Create the blueprint
question_bp = Blueprint("question_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
question_repository = QuestionRepository(db_session)
question_service = QuestionService(question_repository)


@question_bp.route("/create_question/<int:exam_id>", methods=["POST"])
def create_question(exam_id: int):
    """Create a question for an exam"""
    try:
        data = request.json
        question = question_service.create_question(exam_id, data)
        return jsonify({"question": question.to_dict(), "message": "Question created successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error creating question: {str(e)}")
        return jsonify({"error": "Failed to create question"}), 500

@question_bp.route("/get_questions_for_exam/<int:exam_id>", methods=["GET"])
def get_questions_for_exam(exam_id: int):
    """Get questions for an exam"""
    try:
        questions = question_service.get_questions_for_exam(exam_id)
        questions_dicts = [question.to_dict() for question in questions]
        return jsonify({"questions": questions_dicts, "message": "Questions fetched successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error fetching questions: {str(e)}")
        return jsonify({"error": "Failed to fetch questions"}), 500

