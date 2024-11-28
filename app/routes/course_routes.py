"""
This module contains routes for the course model.

It defines a Flask Blueprint for course-related routes and includes functions for
course data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.course_model import Course
from app.repositories.course_repository import CourseRepository
from app.services.course_service import CourseService
from app.models.exam_model import Exam

# Create the blueprint
course_bp = Blueprint("course_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
course_repository = CourseRepository(db_session)
course_service = CourseService(course_repository)

@course_bp.route("/get_exams_for_course/<int:course_id>", methods=["GET"])
def get_exams_for_course(course_id):
    """Get all exams for a course"""
    try:
        exams = course_service.get_exams_for_course(course_id)
        return jsonify({"exams": exams}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching exams for course: {str(e)}")
        return jsonify({"error": "Failed to fetch exams for course"}), 500


@course_bp.route("/add_exam_to_course/<int:course_id>", methods=["POST"])
def add_exam_to_course(course_id):
    """Add an exam to a course"""
    try:
        data = request.json
        exam = Exam(
            exam_name=data.get("exam_name"),
            exam_date=data.get("exam_date"),
            course_id=course_id,
            description=data.get("description"),
            start_time=data.get("start_time"),
            end_time=data.get("end_time"),
            max_attempts=data.get("max_attempts")
        )
        result = course_service.add_exam_to_course(exam)
        return jsonify({"exam": result}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding exam to course: {str(e)}")
        return jsonify({"error": "Failed to add exam to course"}), 500


@course_bp.route("/courses", methods=["GET"])
def get_all_courses():
    """Get all courses"""
    try:
        courses = course_service.get_all_courses()
        return (
            jsonify(
                [
                    {
                        "course_id": course.course_id,
                        "course_name": course.course_name,
                        "course_code": course.course_code,
                        "course_description": course.course_description,
                        "capacity": course.capacity,
                        "teacher_id": course.teacher_id,
                        "is_active": course.is_active,
                        "start_date": course.start_date,
                        "end_date": course.end_date,
                        "created_at": course.created_at,
                        "updated_at": course.updated_at,
                    }
                    for course in courses
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching courses: {str(e)}")
        return jsonify({"error": str(e)}), 500


@course_bp.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """Get specific course"""
    try:
        course = course_service.get_course_by_id(course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404
        return (
            jsonify(
                {
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "course_description": course.course_description,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching course: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
@course_bp.route("/get_course_info/<int:course_id>", methods=["GET"])
def get_course_info(course_id):
    """Get course info for a specific course"""
    try:
        course = course_service.get_course_info(course_id)
        return jsonify({"course": course}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching course info: {str(e)}")
        return jsonify({"error": "Failed to fetch course info"}), 500


@course_bp.route("/add_course", methods=["POST"])
def add_course():
    """Add a new course"""
    try:
        data = request.json
        new_course = Course(
            course_name=data.get("course_name"),
            course_code=data.get("course_code"),
            course_description=data.get("course_description"),
            capacity=data.get("capacity"),
            teacher_id=data.get("teacher_id"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date")
        )
        result = course_service.create_course(new_course)
        return jsonify({"course": result}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding course: {str(e)}")
        return jsonify({"error": "Failed to add course"}), 500


@course_bp.route("/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """Update existing course"""
    try:
        data = request.json
        existing_course = course_service.get_course_by_id(course_id)
        if not existing_course:
            return jsonify({"error": "Course not found"}), 404

        existing_course.course_name = data.get(
            "course_name", existing_course.course_name
        )
        existing_course.course_description = data.get(
            "course_description", existing_course.course_description
        )
        
        existing_course.course_code = data.get("course_code", existing_course.course_code)
        existing_course.capacity = data.get("capacity", existing_course.capacity)
        existing_course.start_date = data.get("start_date", existing_course.start_date)
        existing_course.end_date = data.get("end_date", existing_course.end_date)

        updated_course = course_service.update_course(existing_course)
        return (
            jsonify(
                {
                    "course_id": updated_course.course_id,
                    "course_name": updated_course.course_name,
                    "course_description": updated_course.course_description,
                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating course: {str(e)}")
        return jsonify({"error": str(e)}), 500


@course_bp.route("/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    """Delete existing course"""
    try:
        course = course_service.get_course_by_id(course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404

        course_service.delete_course(course)
        return jsonify({"message": "Course deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting course: {str(e)}")
        return jsonify({"error": str(e)}), 500
