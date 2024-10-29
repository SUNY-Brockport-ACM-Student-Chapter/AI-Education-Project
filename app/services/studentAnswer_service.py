# services/studentAnswer_service.py

from app.models.studentAnswer_model import StudentAnswer
from app.repositories.studentAnswer_repository import StudentAnswerRepository


class StudentAnswerService:
    def __init__(self, student_answer_repo: StudentAnswerRepository):
        self.student_answer_repo = student_answer_repo

    def get_student_answer_by_id(self, student_answer_id: int):
        return self.student_answer_repo.get_student_answer_by_id(student_answer_id)

    def get_all_student_answers(self):
        return self.student_answer_repo.get_all_student_answers()

    def create_student_answer(self, student_answer: StudentAnswer):
        return self.student_answer_repo.create_student_answer(student_answer)

    def update_student_answer(self, student_answer: StudentAnswer):
        return self.student_answer_repo.update_student_answer(student_answer)

    def delete_student_answer(self, student_answer: StudentAnswer):
        return self.student_answer_repo.delete_student_answer(student_answer)
