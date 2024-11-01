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


@student_answer_bp.route("/student_answers", methods=["GET"])
def get_all_student_answers():
    """Get all student answers"""
    try:
        student_answers = student_answer_service.get_all_student_answers()
        return (
            jsonify(
                [
                    {
                        "student_answer_id": student_answer.student_answer_id,
                        "student_id": student_answer.student_id,
                        "question_id": student_answer.question_id,
                        "answer_text": student_answer.answer_text,
                    }
                    for student_answer in student_answers
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching student answers: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["GET"])
def get_student_answer(student_answer_id):
    """Get specific student answer"""
    try:
        student_answer = student_answer_service.get_student_answer_by_id(
            student_answer_id
        )
        if not student_answer:
            return jsonify({"error": "Student answer not found"}), 404
        return (
            jsonify(
                {
                    "student_answer_id": student_answer.student_answer_id,
                    "student_id": student_answer.student_id,
                    "question_id": student_answer.question_id,
                    "answer_text": student_answer.answer_text,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching student answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_answer_bp.route("/student_answers", methods=["POST"])
def create_student_answer():
    """Create a new student answer"""
    try:
        data = request.json
        new_student_answer = StudentAnswer(
            student_id=data.get("student_id"),
            question_id=data.get("question_id"),
            answer_text=data.get("answer_text"),
            answer_grade=data.get("answer_grade", "N"),  # Default grade 'N' for Not graded
            answer_stage=data.get("answer_stage", 1),    # Default to first attempt
            second_attempt_answer=data.get("second_attempt_answer", None),
            second_attempt_grade=data.get("second_attempt_grade", None)
        )
        
        # Validate required fields
        if not all([new_student_answer.student_id, 
                   new_student_answer.question_id, 
                   new_student_answer.answer_text]):
            return jsonify({"error": "Missing required fields"}), 400

        result = student_answer_service.create_student_answer(new_student_answer)
        return (
            jsonify({
                "student_answer_id": result.student_answer_id,
                "student_id": result.student_id,
                "question_id": result.question_id,
                "answer_text": result.answer_text,
                "second_attempt_answer": result.second_attempt_answer,
                "answer_grade": result.answer_grade,
                "second_attempt_grade": result.second_attempt_grade,
                "answer_stage": result.answer_stage
            }),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating student answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["PUT"])
def update_student_answer(student_answer_id):
    """Update existing student answer"""
    try:
        data = request.json
        existing_student_answer = student_answer_service.get_student_answer_by_id(
            student_answer_id
        )
        if not existing_student_answer:
            return jsonify({"error": "Student answer not found"}), 404

        existing_student_answer.student_id = data.get(
            "student_id", existing_student_answer.student_id
        )
        existing_student_answer.question_id = data.get(
            "question_id", existing_student_answer.question_id
        )
        existing_student_answer.answer_text = data.get(
            "answer_text", existing_student_answer.answer_text
        )

        updated_student_answer = student_answer_service.update_student_answer(
            existing_student_answer
        )
        return (
            jsonify(
                {
                    "student_answer_id": updated_student_answer.student_answer_id,
                    "student_id": updated_student_answer.student_id,
                    "question_id": updated_student_answer.question_id,
                    "answer_text": updated_student_answer.answer_text,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating student answer: {str(e)}")
        return jsonify({"error": str(e)}), 500


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["DELETE"])
def delete_student_answer(student_answer_id):
    """Delete existing student answer"""
    try:
        student_answer = student_answer_service.get_student_answer_by_id(
            student_answer_id
        )
        if not student_answer:
            return jsonify({"error": "Student answer not found"}), 404

        student_answer_service.delete_student_answer(student_answer)
        return jsonify({"message": "Student answer deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting student answer: {str(e)}")
        return jsonify({"error": str(e)}), 500
