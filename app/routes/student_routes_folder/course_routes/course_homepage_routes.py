from flask import Blueprint, jsonify
from flask_login import current_user, login_required

from app.services.course_service import CourseService
from app.services.exam_service import ExamService
from app.services.student_service import StudentService

course_homepage_bp = Blueprint("course_homepage", __name__)


@course_homepage_bp.route("/api/courses/<course_id>/homepage", methods=["GET"])
##@login_required
def get_course_homepage_data(course_id):
    """
    Retrieves course homepage data including course details, student info,
    and all exams for the specified course.
    """
    try:
        # Get services
        student_service = StudentService()
        course_service = CourseService()
        exam_service = ExamService()

        # Get student info
        student = student_service.get_student_by_id(current_user.student_id)

        # Get course details
        course = course_service.get_course_by_id(course_id)

        # Verify student is enrolled in the course
        enrolled_courses = course_service.get_courses_for_student(
            current_user.student_id
        )
        if not any(course.course_id == course_id for course in enrolled_courses):
            return jsonify({"error": "Student not enrolled in this course"}), 403

        # Get all exams for the course
        course_exams = exam_service.get_course_exams(course_id)

        return (
            jsonify(
                {
                    "student": {
                        "first_name": student.first_name,
                        "last_name": student.last_name,
                        "initials": f"{student.first_name[0]}{student.last_name[0]}",
                    },
                    "course": {
                        "course_id": course.course_id,
                        "course_name": course.course_name,
                        "course_code": course.course_code,
                        "course_description": course.course_description,
                        "start_date": course.start_date,
                        "end_date": course.end_date,
                        "is_active": course.is_active,
                    },
                    "exams": course_exams,
                }
            ),
            200,
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
