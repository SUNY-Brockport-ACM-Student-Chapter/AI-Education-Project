# repositories/teacher_repository.py

from sqlalchemy.orm import Session

from app.models.teacher_model import Teacher


class TeacherRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_teacher_by_id(self, teacher_id: int):
        """Get a teacher by their ID"""
        teacher = (
            self.session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
        )
        if not teacher:
            raise ValueError("Teacher not found")
        return teacher
