"""
This module initializes and collects all the Flask blueprints for the application.
"""

# Core Blueprints
from app.routes.main_routes import main_bp
from app.routes.user_routes import user_bp

# Educational Blueprints (Renamed/New)
from app.routes.course_routes import course_bp
from app.routes.enrollment_routes import enrollment_bp
from app.routes.question_routes import question_bp
from app.routes.submission_routes import submission_bp # NEW: for /submission
from app.routes.submission_answer_routes import submission_answer_bp # Renamed from student_answer_bp

# Still need to be implemented
# from app.routes.section_routes import section_bp # NEW Placeholder
# from app.routes.file_routes import file_bp # NEW Placeholder
# from app.routes.assessment_routes import assignment_bp # Renamed from assessment_routes
# from app.routes.ai_interaction_routes import ai_bp # Renamed from ai_assessment_routes


# Group related blueprints
core_blueprints = [main_bp]

user_management_blueprints = [
    user_bp,
    enrollment_bp,
]

educational_blueprints = [
    course_bp,
    # section_bp,
    # assessment_bp,
    question_bp,
    submission_bp,
    submission_answer_bp,
]

# ai_blueprints = [ai_bp]

# misc_blueprints = [file_bp]


# Combine all blueprints
all_blueprints = (
    core_blueprints
    + user_management_blueprints
    + educational_blueprints
    # + ai_blueprints
    # + misc_blueprints
)
