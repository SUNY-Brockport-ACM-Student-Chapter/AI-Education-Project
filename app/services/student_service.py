# services/student_service.py

from app.repositories.student_repository import StudentRepository
import json

class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def search_for_students(self, data: dict):
        return self.student_repo.search_for_students(data)

    def get_students_for_course(self, course_id: int):
        return self.student_repo.get_students_for_course(course_id)
    
    def create_student(self, student_data: json):
        return self.student_repo.create_student(student_data)
