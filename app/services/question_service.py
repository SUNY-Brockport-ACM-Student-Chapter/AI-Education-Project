# services/question_service.py

from app.models.question_model import Question
from app.repositories.question_repository import QuestionRepository


class QuestionService:
    def __init__(self, question_repo: QuestionRepository):
        self.question_repo = question_repo


    def get_question_list_for_exam(self, exam_id: int):
        questions = self.question_repo.get_all_questions_for_exam(exam_id)
        return [question.to_dict() for question in questions]


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
    
    
    