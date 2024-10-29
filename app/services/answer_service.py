# services/answer_service.py

from models.answer_model import Answer
from repositories.answer_repository import AnswerRepository


class AnswerService:
    def __init__(self, answer_repo: AnswerRepository):
        self.answer_repo = answer_repo

    def get_answer_by_id(self, answer_id: int):
        return self.answer_repo.get_answer_by_id(answer_id)

    def get_all_answers(self):
        return self.answer_repo.get_all_answers()

    def create_answer(self, answer: Answer):
        return self.answer_repo.create_answer(answer)

    def update_answer(self, answer: Answer):
        return self.answer_repo.update_answer(answer)

    def delete_answer(self, answer: Answer):
        return self.answer_repo.delete_answer(answer)
