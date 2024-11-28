"""
This module contains the routes for the teacher.

It defines a Flask Blueprint for the teacher routes and includes functions for
handling the teacher routes.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.models.teacher_model import Teacher
from app.repositories.teacher_repository import TeacherRepository
from app.services.teacher_service import TeacherService
from app.models.course_model import Course

# Create the blueprint
teacher_bp = Blueprint("teacher_bp", __name__)

# Initialize service with repository
db_session = get_db_session()
teacher_repository = TeacherRepository(db_session)
teacher_service = TeacherService(teacher_repository)


@teacher_bp.route("/get_teacher_dashboard_data/<string:teacher_id>", methods=["GET"])
def get_teacher_dashboard_data(teacher_id):
    """Get dashboard data for a specific teacher"""
    try:
        dashboard_data = teacher_service.get_dashboard_data(teacher_id)
        return jsonify({"dashboard_data": dashboard_data}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching teacher dashboard data: {str(e)}")
        return jsonify({"error": "Failed to fetch dashboard data"}), 500
    
@teacher_bp.route("/get_all_active_courses_for_teacher/<int:teacher_id>", methods=["GET"])
def get_all_active_courses_for_teacher(teacher_id):
    """Get all active courses for a specific teacher"""
    try:
        courses = teacher_service.get_all_active_courses_for_teacher(teacher_id)
        return jsonify({"courses": courses}), 200  
    except Exception as e:
        current_app.logger.error(f"Error fetching active courses: {str(e)}")
        return jsonify({"error": "Failed to fetch active courses"}), 500

@teacher_bp.route("/get_all_inactive_courses_for_teacher/<int:teacher_id>", methods=["GET"])
def get_all_inactive_courses_for_teacher(teacher_id):
    """Get all inactive courses for a specific teacher"""
    try:
        courses = teacher_service.get_all_inactive_courses_for_teacher(teacher_id)
        return jsonify({"courses": courses}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching inactive courses: {str(e)}")
        return jsonify({"error": "Failed to fetch inactive courses"}), 500



@teacher_bp.route("/search_for_student/<string:search_query>", methods=["GET"])
def search_for_student(search_query):
    """Search for a student by name"""
    try:
        students = teacher_service.search_for_student(search_query)
        return jsonify({"students": students}), 200
    except Exception as e:
        current_app.logger.error(f"Error searching for student: {str(e)}")
        return jsonify({"error": "Failed to search for student"}), 500


@teacher_bp.route("/get_all_teachers", methods=["GET"])
def get_all_teachers():
    """Get all teachers"""
    try:
        teachers = teacher_service.get_all_teachers()
        return (
            jsonify(
                [
                    {
                        "teacher_id": teacher.teacher_id,
                        "first_name": teacher.first_name,
                        "last_name": teacher.last_name,
                        "email": teacher.email,
                    }
                    for teacher in teachers
                ]
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching teachers: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/get_teacher_by_id/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    """Get specific teacher"""
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not teacher:
            return jsonify({"error": "Teacher not found"}), 404
        return (
            jsonify(
                {"teacher_id": teacher.teacher_id, "teacher_name": teacher.teacher_name}
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/create_teacher", methods=["POST"])
def create_teacher():
    """Create a new teacher"""
    try:
        data = request.json
        new_teacher = Teacher(
            clerk_user_id=data.get("clerk_user_id"),
            user_name=data.get("user_name"),
            email=data.get("email"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name")
            )
        result = teacher_service.create_teacher(new_teacher)
        return (
            jsonify(
                {
                    "teacher_id": result.teacher_id,
                    "student_name": result.first_name + " " + result.last_name

                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(f"Error creating teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/update_teacher_by_id/<int:teacher_id>", methods=["PUT"])
def update_teacher(teacher_id):
    """Update existing teacher"""
    try:
        data = request.json
        existing_teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not existing_teacher:
            return jsonify({"error": "Teacher not found"}), 404
        
        if "clerk_user_id" in data:
            existing_teacher.clerk_user_id = data["clerk_user_id"]
        if "user_name" in data:
            existing_teacher.user_name = data["user_name"]
        if "email" in data:
            existing_teacher.email = data["email"]
        if "first_name" in data:
            existing_teacher.first_name = data["first_name"]
        if "last_name" in data:
            existing_teacher.last_name = data["last_name"]
        if "is_active" in data:
            existing_teacher.is_active = data["is_active"]
        if "last_login" in data:
            existing_teacher.last_login = data["last_login"]

        updated_teacher = teacher_service.update_teacher(existing_teacher)
        
        return (
            jsonify(
                {
                    "teacher_id": updated_teacher.teacher_id,
                    "user_name": updated_teacher.user_name,
                    "email": updated_teacher.email,
                    "first_name": updated_teacher.first_name,
                    "last_name": updated_teacher.last_name,
                    "is_active": updated_teacher.is_active,
                    "last_login": updated_teacher.last_login.isoformat() if updated_teacher.last_login else None,
                    "created_at": updated_teacher.created_at.isoformat() if updated_teacher.created_at else None,
                    "updated_at": updated_teacher.updated_at.isoformat() if updated_teacher.updated_at else None,
               

                }
            ),
            200,
        )
    except Exception as e:
        current_app.logger.error(f"Error updating teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500


@teacher_bp.route("/delete_teacher_by_id/<int:teacher_id>", methods=["DELETE"])
def delete_teacher(teacher_id):
    """Delete existing teacher"""
    try:
        teacher = teacher_service.get_teacher_by_id(teacher_id)
        if not teacher:
            return jsonify({"error": "Teacher not found"}), 404

        teacher_service.delete_teacher(teacher)
        return jsonify({"message": "Teacher deleted successfully"}), 200
    except Exception as e:
        current_app.logger.error(f"Error deleting teacher: {str(e)}")
        return jsonify({"error": str(e)}), 500
