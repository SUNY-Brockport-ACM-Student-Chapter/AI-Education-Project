# repositories/teacher_repository.py

from sqlalchemy.orm import Session

from app.models.teacher_model import Teacher

class TeacherRepository:
    def __init__(self, session: Session):
        self.session = session


    def get_teacher_by_clerk_user_id(self, clerk_user_id: str):
        return self.session.query(Teacher).filter(Teacher.clerk_user_id == clerk_user_id).first()
    