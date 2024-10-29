# services/teacher_service.py

from app.models.teacher_model import Teacher
from app.repositories.teacher_repository import TeacherRepository


class TeacherService:
    def __init__(self, teacher_repo: TeacherRepository):
        self.teacher_repo = teacher_repo

    def get_teacher_by_id(self, teacher_id: int):
        return self.teacher_repo.get_teacher_by_id(teacher_id)

    def get_all_teachers(self):
        return self.teacher_repo.get_all_teachers()

    def create_teacher(self, teacher: Teacher):
        return self.teacher_repo.create_teacher(teacher)

    def update_teacher(self, teacher: Teacher):
        return self.teacher_repo.update_teacher(teacher)

    def delete_teacher(self, teacher: Teacher):
        return self.teacher_repo.delete_teacher(teacher)
