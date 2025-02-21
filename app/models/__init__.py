from app.models.ai_assessment_model import AiAssessment
from app.models.answer_model import Answer
from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.exam_model import Exam

from app.models.question_model import Question
from app.models.student_model import Student
from app.models.studentAnswer_model import StudentAnswer
from app.models.teacher_model import Teacher

__all__ = [
    "Exam",
    "Question",
    "Answer",
    "Course",
    "Enrollment",
    "Teacher",
    "Student",
    "StudentAnswer",
    "AiAssessment",
]
