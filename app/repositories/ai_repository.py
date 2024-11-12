# repositories/ai_repository.py

"""
This module contains the repository for the AI model.
"""

from sqlalchemy.orm import Session

from app.models.ai_assessment_model import AIAssessment


class AIRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_ai_by_id(self, ai_id: int):
        return (
            self.session.query(AIAssessment).filter(AIAssessment.ai_id == ai_id).first()
        )

    def get_all_ais(self):
        return self.session.query(AIAssessment).all()

    def create_ai(self, ai: AIAssessment):
        self.session.add(ai)
        self.session.commit()
        return ai

    def update_ai(self, ai: AIAssessment):
        self.session.merge(ai)
        self.session.commit()
        return ai

    def delete_ai(self, ai: AIAssessment):
        self.session.delete(ai)
        self.session.commit()
