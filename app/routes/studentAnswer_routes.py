"""
This module contains the routes for the student answers.

It defines a Flask Blueprint for the student answer routes and includes functions for
handling the student answer routes.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.studentAnswer_model import StudentAnswer
from app.repositories.studentAnswer_repository import StudentAnswerRepository
from app.services.studentAnswer_service import StudentAnswerService

# Create the blueprint
student_answer_bp = Blueprint("student_answer_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
student_answer_repository = StudentAnswerRepository(db_session)
student_answer_service = StudentAnswerService(student_answer_repository)


@student_answer_bp.route("/get_student_answers_for_student/<int:student_id>/<int:question_id>", methods=["GET"])
def get_student_answers_for_student(student_id: int, question_id: int):
    """Get student answers for a student"""
    try:
        student_answers = student_answer_service.get_student_answers_for_student(student_id, question_id)
        student_answers_dict = [student_answer.to_dict() for student_answer in student_answers]
        return jsonify({"student_answers": student_answers_dict}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error fetching student answers: {str(e)}")
        return jsonify({"error": "Failed to fetch student answers"}), 500
    
@student_answer_bp.route("/create_student_answer/<int:student_id>/<int:question_id>", methods=["POST"])
def create_student_answer(student_id: int, question_id: int):
    """Create a student answer"""
    try:
        student_answer = student_answer_service.create_student_answer(student_id, question_id, request.json)  
        return jsonify({"student_answer": student_answer.to_dict()}), 200
    except Exception as e:
        current_app.logger.error(f"Error creating student answer: {str(e)}")
        return jsonify({"error": "Failed to create student answer"}), 500

