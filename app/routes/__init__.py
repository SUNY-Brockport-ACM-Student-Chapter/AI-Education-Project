"""
This module initializes and collects all the Flask blueprints for the application.

It imports the blueprints from their respective modules and creates a list
of all blueprints for easy registration in the main application factory.
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

# Define a list of all blueprints for easy registration
all_blueprints = [
    student_bp,
    ai_bp,
    course_bp,
    exam_bp,
    main_bp,
    user_bp,
    enrollment_bp,
    question_bp,
    student_answer_bp,
    teacher_bp,
    answer_bp,
]
