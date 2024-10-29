"""
This module initializes and collects all the Flask blueprints for the application.
"""

from .ai_routes import ai_bp
from .answer_routes import answer_bp
from .course_routes import course_bp
from .enrollment_routes import enrollment_bp
from .exam_routes import exam_bp
from .main_routes import main_bp
from .question_routes import question_bp
from .student_routes import student_bp
from .studentAnswer_routes import student_answer_bp
from .teacher_routes import teacher_bp
from .user_routes import user_bp

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
