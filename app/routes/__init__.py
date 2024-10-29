"""
This module initializes and collects all the Flask blueprints for the application.
"""

from app.routes.ai_routes import ai_bp
from app.routes.answer_routes import answer_bp
from app.routes.course_routes import course_bp
from app.routes.enrollment_routes import enrollment_bp
from app.routes.exam_routes import exam_bp
from app.routes.main_routes import main_bp
from app.routes.question_routes import question_bp
from app.routes.student_routes import student_bp
from app.routes.studentAnswer_routes import student_answer_bp
from app.routes.teacher_routes import teacher_bp
from app.routes.user_routes import user_bp

# Group related blueprints
core_blueprints = [main_bp, user_bp]

educational_blueprints = [
    course_bp,
    exam_bp,
    question_bp,
    answer_bp,
]

user_management_blueprints = [
    student_bp,
    teacher_bp,
    enrollment_bp,
    student_answer_bp,
]

ai_blueprints = [ai_bp]

# Combine all blueprints
all_blueprints = (
    core_blueprints
    + educational_blueprints
    + user_management_blueprints
    + ai_blueprints
)
