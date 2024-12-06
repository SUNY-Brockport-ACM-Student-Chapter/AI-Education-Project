# services/teacher_service.py

from app.repositories.teacher_repository import TeacherRepository


class TeacherService:
    def __init__(self, teacher_repo: TeacherRepository):
        self.teacher_repo = teacher_repo


    def get_teacher_by_id(self, teacher_id: int):
        return self.teacher_repo.get_teacher_by_id(teacher_id)