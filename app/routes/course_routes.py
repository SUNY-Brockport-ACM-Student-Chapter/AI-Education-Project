"""
This module contains routes for the course model.

It defines a Flask Blueprint for course-related routes and includes functions for
course data processing.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.course_model import Course
from app.models.exam_model import Exam
from app.repositories.course_repository import CourseRepository
from app.services.course_service import CourseService

# Create the blueprint
course_bp = Blueprint("course_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
course_repository = CourseRepository(db_session)
course_service = CourseService(course_repository)


@course_bp.route("/get_active_courses_for_teacher/<int:teacher_id>", methods=["GET"])
def get_active_courses_for_teacher(teacher_id):
    """Get all active courses for a teacher"""
    try:
        courses = course_service.get_active_courses_for_teacher(teacher_id)
        courses_list = []
        for course in courses:
            courses_list.append(course.to_dict())
        return jsonify({"courses": courses_list}), 200
    except ValueError as e:
        current_app.logger.error(f"Error fetching active courses for teacher: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error fetching active courses for teacher: {str(e)}")
        return jsonify({"error": "Failed to fetch active courses for teacher"}), 500


@course_bp.route("/create_course/<int:teacher_id>", methods=["POST"])
def create_course(teacher_id):
    """Create a course"""
    try:
        course = course_service.create_course(teacher_id, request.json)
        return (
            jsonify(
                {"message": "Course created successfully", "course": course.to_dict()}
            ),
            200,
        )
    except ValueError as e:
        current_app.logger.error(f"Error creating course: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error creating course: {str(e)}")
        return jsonify({"error": "Failed to create course"}), 500


@course_bp.route("/update_course/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    """Update a course"""
    try:
        course = course_service.update_course(course_id, request.json)
        return (
            jsonify(
                {"message": "Course updated successfully", "course": course.to_dict()}
            ),
            200,
        )
    except ValueError as e:
        current_app.logger.error(f"Error updating course: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error updating course: {str(e)}")
        return jsonify({"error": "Failed to update course"}), 500


@course_bp.route("/change_course_status/<int:course_id>", methods=["PUT"])
def change_course_status(course_id):
    """Change the status of a course"""
    try:
        course = course_service.change_course_status(course_id)
        return (
            jsonify(
                {
                    "message": "Course status changed successfully",
                    "course": course.to_dict(),
                }
            ),
            200,
        )
    except ValueError as e:
        current_app.logger.error(f"Error changing course status: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error changing course status: {str(e)}")
        return jsonify({"error": "Failed to change course status"}), 500


@course_bp.route("/get_active_courses_for_student/<int:student_id>", methods=["GET"])
def get_active_courses_for_student(student_id):
    """Get all active courses for a student"""
    try:
        courses = course_service.get_active_courses_for_student(student_id)
        courses_list = []
        for course in courses:
            courses_list.append(course.to_dict())
        return jsonify({"courses": courses_list}), 200
    except ValueError as e:
        current_app.logger.error(f"Error fetching active courses for student: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error fetching active courses for student: {str(e)}")
        return jsonify({"error": "Failed to fetch active courses for student"}), 500
