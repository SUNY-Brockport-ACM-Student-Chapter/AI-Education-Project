"""
This module contains routes for the course model.

It defines a Flask Blueprint for course-related routes and includes functions for
course data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from database import get_db_session
from models.course_model import Course
from repositories.course_repository import CourseRepository
from services.course_service import CourseService

# Create the blueprint
course_bp = Blueprint("course_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
course_repository = CourseRepository(db_session)
course_service = CourseService(course_repository)


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
                        "course_description": course.course_description,
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


@course_bp.route("/courses", methods=["POST"])
def create_course():
    """Create a new course"""
    try:
        data = request.json
        new_course = Course(
            course_name=data.get("course_name"),
            course_description=data.get("course_description"),
        )
        result = course_service.create_course(new_course)
        return (
            jsonify(
                {
                    "course_id": result.course_id,
                    "course_name": result.course_name,
                    "course_description": result.course_description,
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating course: {str(e)}")
        return jsonify({"error": str(e)}), 500


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
