from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.exam_service import ExamService
from app.database import get_db_session
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.exam_repository import ExamRepository


dashboard_bp = Blueprint('dashboard', __name__)


# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
course_repository = CourseRepository(db_session)
exam_repository = ExamRepository(db_session)


student_service = StudentService(student_repository)
course_service = CourseService(course_repository)
exam_service = ExamService(exam_repository)


@dashboard_bp.route('/dashboard', methods=['GET'])
##@login_required
def get_dashboard_data():
    """
    Retrieves dashboard data including upcoming exams and enrolled courses
    for the currently logged-in student.
    """
    try:
        student_id = 101
        # Get student info
        student = student_service.get_student_by_id(student_id)
        #student = student_service.get_student_id_by_user_id(current_user.user_id)

        # Get student's upcoming exams
        upcoming_exams = exam_service.get_upcoming_exams_for_student(student_id)
        #upcoming_exams = exam_service.get_upcoming_exams_for_student(current_user.student_id)
        
        # Get student's enrolled courses
        enrolled_courses = course_service.get_courses_for_student(student_id)
        #enrolled_courses = course_service.get_courses_for_student(current_user.student_id)

        return jsonify({
            'first_name': student.first_name,
            'last_name': student.last_name,
            'initials': f"{student.first_name[0]}{student.last_name[0]}",
            'upcoming_exams': upcoming_exams,
            'enrolled_courses': enrolled_courses
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
