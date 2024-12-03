# services/student_service.py

from app.repositories.student_repository import StudentRepository



class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def search_for_students(self, search_query: str):
        return self.student_repo.search_for_students(search_query)
    
    def get_students_for_course(self, course_id: int):
        return self.student_repo.get_students_for_course(course_id)

