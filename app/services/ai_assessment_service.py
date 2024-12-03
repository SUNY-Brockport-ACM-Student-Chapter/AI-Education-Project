# services/ai_service.py

"""
This module contains the service for the AI model.
"""

from app.repositories.ai_assessment_repository import AiAssessmentRepository


class AiAssessmentService:
    def __init__(self, ai_repo: AiAssessmentRepository):
        self.ai_repo = ai_repo

    def get_ai_assesment_for_studentAnswer(self, studentAnswer_id: int):
        return self.ai_repo.get_ai_assesment_for_studentAnswer(studentAnswer_id)
