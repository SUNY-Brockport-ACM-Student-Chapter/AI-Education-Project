# services/question_service.py

from models.question_model import Question
from repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self, question_repo: QuestionRepository):
        self.question_repo = question_repo

    def get_question_by_id(self, question_id: int):
        return self.question_repo.get_question_by_id(question_id)

    def get_all_questions(self):
        return self.question_repo.get_all_questions()

    def create_question(self, question: Question):
        return self.question_repo.create_question(question)

    def update_question(self, question: Question):
        return self.question_repo.update_question(question)

    def delete_question(self, question: Question):
        return self.question_repo.delete_question(question)
