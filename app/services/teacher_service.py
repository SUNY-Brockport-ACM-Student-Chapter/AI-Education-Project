# services/teacher_service.py

from app.repositories.teacher_repository import TeacherRepository


class TeacherService:
    def __init__(self, teacher_repo: TeacherRepository):
        self.teacher_repo = teacher_repo

    
    def search_for_student(self, search_query: str):
        return self.teacher_repo.search_for_student(search_query)
    
    