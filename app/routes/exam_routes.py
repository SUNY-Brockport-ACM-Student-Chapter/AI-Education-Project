"""
This module contains routes for the exam model. 

It defines a Flask Blueprint for exam-related routes and includes functions for
exam data processing.
"""

from flask import Blueprint, current_app, jsonify, request

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
        exam_dicts = []
        for exam in exams:
            exam_dicts.append(exam.to_dict())
        return jsonify({"exams": exam_dicts}), 200
    except ValueError as e:
        current_app.logger.error(f"Error getting exams for teacher: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error getting exams for teacher: {str(e)}")
        return jsonify({"error": "Failed to get exams for teacher"}), 500
    
@exam_bp.route("/get_exams_for_course/<int:course_id>", methods=["GET"])
def get_exams_for_course(course_id: int):
    """Get exams for a course"""
    try:
        exams = exam_service.get_exams_for_course(course_id)
        exam_dicts = []
        for exam in exams:
            exam_dicts.append(exam.to_dict())
        return jsonify({"exams": exam_dicts}), 200
    except ValueError as e:
        current_app.logger.error(f"Error getting exams for course: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error getting exams for course: {str(e)}")
        return jsonify({"error": "Failed to get exams for course"}), 500
    
@exam_bp.route("/create_exam_for_course/<int:course_id>", methods=["POST"])
def create_exam_for_course(course_id: int):    
    """Create an exam for a course"""
    try:
        data = request.json
        exam = exam_service.create_exam(course_id, data)
        return jsonify({"exam": exam.to_dict(), "message": "Exam created successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error creating exam: {str(e)}")
        return jsonify({"error": "Failed to create exam"}), 500
    

@exam_bp.route("/get_student_exam_submission_stage/<int:exam_id>/<int:student_id>", methods=["GET"])
def get_student_exam_submission_stage(exam_id: int, student_id: int):
    """Get the submission stage for a student in an exam"""
    try:
        stage = exam_service.get_student_exam_submission_stage(exam_id, student_id)
        return jsonify({"stage": stage}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error getting exam submission stage: {str(e)}")
        return jsonify({"error": "Failed to get exam submission stage"}), 500

@exam_bp.route("/get_exams_for_student/<int:student_id>", methods=["GET"])
def get_exams_for_student(student_id: int):
    """Get exams for a student"""
    try:
        exams = exam_service.get_exams_for_student(student_id)
        exam_dicts = []
        for exam in exams:
            exam_dicts.append(exam.to_dict())
        return jsonify({"exams": exam_dicts, "message": "Exams fetched successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Error getting exams for student: {str(e)}")
        return jsonify({"error": "Failed to get exams for student"}), 500
