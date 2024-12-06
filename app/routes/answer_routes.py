"""
This module contains routes for the answer model. 
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.answer_repository import AnswerRepository
from app.services.answer_service import AnswerService

# Create the blueprint
answer_bp = Blueprint("answer_bp", __name__)

# Initialize service with repository
db_session = get_db_session()

answer_repository = AnswerRepository(db_session)

answer_service = AnswerService(answer_repository)


@answer_bp.route("/create_answer/<int:question_id>", methods=["POST"])
def create_answer(question_id: int):
    """Create an answer for a question"""
    try:
        data = request.json
        answer_text = data.get("answer_text")
        answer = answer_service.create_answer(question_id, answer_text)
        return jsonify({"message": "Answer created successfully", "answer": answer.to_dict()}), 201
    except Exception as e:
        current_app.logger.error(f"Error creating answer: {str(e)}")
        return jsonify({"error": str(e)}), 500
