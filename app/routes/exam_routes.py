"""
This module contains routes for the exam model. 

It defines a Flask Blueprint for exam-related routes and includes functions for
exam data processing.
"""

from flask import Blueprint, current_app, jsonify

from app.database import get_db_session
from app.repositories.exam_repository import ExamRepository
from app.services.exam_service import ExamService

# Create the blueprint
exam_bp = Blueprint("exam_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
exam_repository = ExamRepository(db_session)
exam_service = ExamService(exam_repository)

@exam_bp.route("/get_exams_for_teacher/<int:teacher_id>", methods=["GET"])
def get_exams_for_teacher(teacher_id: int):
    """Get exams for a teacher"""
    try:
        exams = exam_service.get_exams_for_teacher(teacher_id)
        return jsonify({"exams": exams}), 200
    except Exception as e:
        current_app.logger.error(f"Error getting exams for teacher: {str(e)}")
        return jsonify({"error": "Failed to get exams for teacher"}), 500
    
@exam_bp.route("/get_exams_for_course/<int:course_id>", methods=["GET"])
def get_exams_for_course(course_id: int):
    """Get exams for a course"""
    try:
        exams = exam_service.get_exams_for_course(course_id)
        return jsonify({"exams": exams}), 200
    except Exception as e:
        current_app.logger.error(f"Error getting exams for course: {str(e)}")
        return jsonify({"error": "Failed to get exams for course"}), 500
    
@exam_bp.route("/create_exam/<int:course_id>", methods=["POST"])
def create_exam(course_id: int):
    """Create an exam"""
    try:
        exam = exam_service.create_exam(course_id)
        return jsonify({"exam": exam}), 201
    except Exception as e:
        current_app.logger.error(f"Error creating exam: {str(e)}")
        return jsonify({"error": "Failed to create exam"}), 500
    

@exam_bp.route("/get_exam_submission_number/<int:exam_id>/<int:student_id>", methods=["GET"])
def get_exam_submission_number(exam_id: int, student_id: int):
    """Get the number of submissions for an exam"""
    try:
        number = exam_service.get_exam_submission_number(exam_id, student_id)
        return jsonify({"number": number}), 200
    except Exception as e:
        current_app.logger.error(f"Error getting exam submission number: {str(e)}")
        return jsonify({"error": "Failed to get exam submission number"}), 500

@exam_bp.route("/get_exams_for_student/<int:student_id>", methods=["GET"])
def get_exams_for_student(student_id: int):
    """Get exams for a student"""
    try:
        exams = exam_service.get_exams_for_student(student_id)
        return jsonify({"exams": exams}), 200
    except Exception as e:
        current_app.logger.error(f"Error getting exams for student: {str(e)}")
        return jsonify({"error": "Failed to get exams for student"}), 500
