# services/studentAnswer_service.py

from app.models.studentAnswer_model import StudentAnswer
from app.repositories.studentAnswer_repository import StudentAnswerRepository


class StudentAnswerService:
    def __init__(self, student_answer_repo: StudentAnswerRepository):
        self.student_answer_repo = student_answer_repo

    def get_student_answers_for_student(self, student_id: int, question_id: int):
        return self.student_answer_repo.get_student_answers_for_student(student_id, question_id)
    
    def create_student_answer(self, student_id: int, question_id: int):
        return self.student_answer_repo.create_student_answer(student_id, question_id)


    def get_student_answer_by_id(self, student_answer_id: int):
        return self.student_answer_repo.get_student_answer_by_id(student_answer_id)


