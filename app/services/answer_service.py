# services/answer_service.py

from app.repositories.answer_repository import AnswerRepository


class AnswerService:
    def __init__(self, answer_repo: AnswerRepository):
        self.answer_repo = answer_repo

    def create_answer(self, question_id: int, answer_text: str):
        return self.answer_repo.create_answer(question_id, answer_text)
