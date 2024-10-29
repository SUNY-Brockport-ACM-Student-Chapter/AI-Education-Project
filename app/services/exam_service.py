# services/exam_service.py

from app.models.exam_model import Exam
from app.repositories.exam_repository import ExamRepository


class ExamService:
    def __init__(self, exam_repo: ExamRepository):
        self.exam_repo = exam_repo

    def get_exam_by_id(self, exam_id: int):
        return self.exam_repo.get_exam_by_id(exam_id)

    def get_all_exams(self):
        return self.exam_repo.get_all_exams()

    def create_exam(self, exam: Exam):
        return self.exam_repo.create_exam(exam)

    def update_exam(self, exam: Exam):
        return self.exam_repo.update_exam(exam)

    def delete_exam(self, exam: Exam):
        return self.exam_repo.delete_exam(exam)
