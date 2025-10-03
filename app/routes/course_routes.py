"""
This module contains routes for the course model, following the /course RESTful pattern.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.course_repository import CourseRepository
from app.services.course_service import CourseService

# Create the blueprint with RESTful prefix
course_bp = Blueprint("course_bp", __name__, url_prefix="/course")

# Initialize service with repository
db_session = get_db_session()
course_repository = CourseRepository(db_session)
course_service = CourseService(course_repository)


@course_bp.route("/", methods=["POST"])
def create_course():
    """POST /course: Create a new course."""
    try:
        data = request.json
        if not data or not data.get("teacher_id"):
            return jsonify({"error": "Missing 'teacher_id' or JSON data"}), 400

        teacher_id = data["teacher_id"]
        # Assuming create_course handles the rest of the data
        course = course_service.create_course(teacher_id, data)
        return jsonify({"id": course.id, "message": "Course created successfully"}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating course: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating course: {str(e)}")
        return jsonify({"error": "Failed to create course"}), 500


@course_bp.route("/<string:course_id>", methods=["GET", "PATCH", "DELETE"])
def handle_course(course_id: str):
    """Handle GET, PATCH, and DELETE operations for a single Course."""
    try:
        if request.method == "GET":
            course = course_service.get_course_by_id(course_id)
            if not course:
                return jsonify({"error": "Course not found"}), 404
            return jsonify(course.to_dict()), 200

        elif request.method == "PATCH":
            data = request.json
            if not data:
                return jsonify({"error": "Missing JSON data for update"}), 400

            course = course_service.update_course(course_id, data)
            return jsonify(course.to_dict()), 200

        elif request.method == "DELETE":
            course_service.delete_course(course_id)
            return "", 204
            
    except ValueError as e:
        current_app.logger.error(f"Error handling course {course_id}: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error handling course: {str(e)}")
        return jsonify({"error": "Failed to process course request"}), 500


@course_bp.route("/", methods=["GET"])
def get_courses_filtered():
    """GET /course?teacher_id=...&student_id=...: Get a list of courses based on query filters."""
    try:
        teacher_id = request.args.get("teacher_id")
        student_id = request.args.get("student_id")

        if teacher_id:
            courses = course_service.get_active_courses_for_teacher(teacher_id)
        elif student_id:
            courses = course_service.get_active_courses_for_student(student_id)
        else:
            # You might return a paginated list of all courses here if no filter is provided
            return jsonify({"error": "Missing required filter query parameter (teacher_id or student_id)"}), 400

        courses_list = [course.to_dict() for course in courses]
        return jsonify({"courses": courses_list}), 200
        
    except ValueError as e:
        current_app.logger.error(f"Error fetching filtered courses: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error fetching filtered courses: {str(e)}")
        return jsonify({"error": "Failed to fetch courses"}), 500


# Dedicated endpoint for status change (using PUT for a full state change on the status field)
@course_bp.route("/<string:course_id>/status", methods=["PUT"])
def change_course_status(course_id: str):
    """PUT /course/{id}/status: Toggle the status of a course (e.g., active/inactive)."""
    try:
        # Assuming the service handles reading the current status and toggling it
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
        current_app.logger.error(f"Internal error changing course status: {str(e)}")
        return jsonify({"error": "Failed to change course status"}), 500
