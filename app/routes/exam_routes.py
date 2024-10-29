"""
This module contains routes for the exam model. 

It defines a Flask Blueprint for exam-related routes and includes functions for
exam data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.exam_model import Exam
from app.repositories.exam_repository import ExamRepository
from app.services.exam_service import ExamService

# Create the blueprint
exam_bp = Blueprint("exam_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
exam_repository = ExamRepository(db_session)
exam_service = ExamService(exam_repository)


@exam_bp.route("/exams", methods=["GET"])
def get_all_exams():
    """Get all exams"""
    try:
        exams = exam_service.get_all_exams()
        return (
            jsonify(
                [
                    {
                        "exam_id": exam.exam_id,
                        "exam_name": exam.exam_name,
                        "course_id": exam.course_id,
                    }
                    for exam in exams
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching exams: {str(e)}")
        return jsonify({"error": str(e)}), 500


@exam_bp.route("/exams/<int:exam_id>", methods=["GET"])
def get_exam(exam_id):
    """Get specific exam"""
    try:
        exam = exam_service.get_exam_by_id(exam_id)
        if not exam:
            return jsonify({"error": "Exam not found"}), 404
        return (
            jsonify(
                {
                    "exam_id": exam.exam_id,
                    "exam_name": exam.exam_name,
                    "course_id": exam.course_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching exam: {str(e)}")
        return jsonify({"error": str(e)}), 500


@exam_bp.route("/exams", methods=["POST"])
def create_exam():
    """Create a new exam"""
    try:
        data = request.json
        new_exam = Exam(
            exam_name=data.get("exam_name"), course_id=data.get("course_id")
        )
        result = exam_service.create_exam(new_exam)
        return (
            jsonify(
                {
                    "exam_id": result.exam_id,
                    "exam_name": result.exam_name,
                    "course_id": result.course_id,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating exam: {str(e)}")
        return jsonify({"error": str(e)}), 500


@exam_bp.route("/exams/<int:exam_id>", methods=["PUT"])
def update_exam(exam_id):
    """Update existing exam"""
    try:
        data = request.json
        existing_exam = exam_service.get_exam_by_id(exam_id)
        if not existing_exam:
            return jsonify({"error": "Exam not found"}), 404

        existing_exam.exam_name = data.get("exam_name", existing_exam.exam_name)
        existing_exam.course_id = data.get("course_id", existing_exam.course_id)

        updated_exam = exam_service.update_exam(existing_exam)
        return (
            jsonify(
                {
                    "exam_id": updated_exam.exam_id,
                    "exam_name": updated_exam.exam_name,
                    "course_id": updated_exam.course_id,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating exam: {str(e)}")
        return jsonify({"error": str(e)}), 500


@exam_bp.route("/exams/<int:exam_id>", methods=["DELETE"])
def delete_exam(exam_id):
    """Delete existing exam"""
    try:
        exam = exam_service.get_exam_by_id(exam_id)
        if not exam:
            return jsonify({"error": "Exam not found"}), 404

        exam_service.delete_exam(exam)
        return jsonify({"message": "Exam deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting exam: {str(e)}")
        return jsonify({"error": str(e)}), 500
