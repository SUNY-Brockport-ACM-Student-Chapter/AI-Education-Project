# services/student_service.py

from models.student_model import Student
from repositories.student_repository import StudentRepository


class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def get_student_by_id(self, student_id: int):
        return self.student_repo.get_student_by_id(student_id)

    def get_all_students(self):
        return self.student_repo.get_all_students()

    def create_student(self, student: Student):
        return self.student_repo.create_student(student)

    def update_student(self, student: Student):
        return self.student_repo.update_student(student)

    def delete_student(self, student: Student):
        return self.student_repo.delete_student(student)