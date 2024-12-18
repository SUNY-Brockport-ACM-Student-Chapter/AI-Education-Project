# repositories/ai_repository.py

"""
This module contains the repository for the AI model.
"""

from sqlalchemy.orm import Session

from app.models.ai_assessment_model import AiAssessment
from app.models.studentAnswer_model import StudentAnswer


class AiAssessmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_ai_assesment_for_studentAnswer(self, studentAnswer_id: int):
        student_answer = (
            self.session.query(StudentAnswer)
            .filter(StudentAnswer.student_answer_id == studentAnswer_id)
            .first()
        )
        if not student_answer:
            raise ValueError("Student answer not found")

        ai_assesment = (
            self.session.query(AiAssessment)
            .filter(AiAssessment.student_answer_id == studentAnswer_id)
            .first()
        )
        return ai_assesment
