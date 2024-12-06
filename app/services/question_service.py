# services/question_service.py

from app.models.question_model import Question
from app.repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self, question_repo: QuestionRepository):
        self.question_repo = question_repo

    def get_questions_for_exam(self, exam_id: int):
        return self.question_repo.get_questions_for_exam(exam_id)

    def create_question(self, exam_id: int, data: dict):
        return self.question_repo.create_question(exam_id, data)
