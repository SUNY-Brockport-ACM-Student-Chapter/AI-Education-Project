# services/ai_service.py

from models.ai_model import Ai
from repositories.ai_repository import AiRepository


class AiService:
    def __init__(self, ai_repo: AiRepository):
        self.ai_repo = ai_repo

    def get_ai_by_id(self, ai_id: int):
        return self.ai_repo.get_ai_by_id(ai_id)

    def get_all_ais(self):
        return self.ai_repo.get_all_ais()

    def create_ai(self, ai: Ai):
        return self.ai_repo.create_ai(ai)

    def update_ai(self, ai: Ai):
        return self.ai_repo.update_ai(ai)

    def delete_ai(self, ai: Ai):
        return self.ai_repo.delete_ai(ai)
