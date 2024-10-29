# repositories/ai_repository.py

from sqlalchemy.orm import Session

from models.ai_model import Ai


class AIRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_ai_by_id(self, ai_id: int):
        return self.session.query(Ai).filter(Ai.ai_id == ai_id).first()

    def get_all_ais(self):
        return self.session.query(Ai).all()

    def create_ai(self, ai: Ai):
        self.session.add(ai)
        self.session.commit()
        return ai

    def update_ai(self, ai: Ai):
        self.session.merge(ai)
        self.session.commit()
        return ai

    def delete_ai(self, ai: Ai):
        self.session.delete(ai)
        self.session.commit()
