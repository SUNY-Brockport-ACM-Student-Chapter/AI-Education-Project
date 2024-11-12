# services/ai_service.py

"""
This module contains the service for the AI model.
"""

from app.models.ai_assessment_model import AiAssessment
from app.repositories.ai_assessment_repository import AiAssessmentRepository


class AiAssessmentService:
    def __init__(self, ai_repo: AiAssessmentRepository):
        self.ai_repo = ai_repo

    def get_ai_by_id(self, ai_id: int):
        return self.ai_repo.get_ai_by_id(ai_id)

    def get_all_ais(self):
        return self.ai_repo.get_all_ais()

    def create_ai(self, ai: AiAssessment):
        return self.ai_repo.create_ai(ai)

    def update_ai(self, ai: AiAssessment):
        return self.ai_repo.update_ai(ai)

    def delete_ai(self, ai: AiAssessment):
        return self.ai_repo.delete_ai(ai)
