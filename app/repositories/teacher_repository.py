# repositories/teacher_repository.py

from sqlalchemy.orm import Session

from models import Teacher


class TeacherRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_teacher_by_id(self, teacher_id: int):
        return self.session.query(Teacher).filter(Teacher.id == teacher_id).first()

    def get_all_teachers(self):
        return self.session.query(Teacher).all()

    def create_teacher(self, teacher: Teacher):
        self.session.add(teacher)
        self.session.commit()
        return teacher

    def update_teacher(self, teacher: Teacher):
        self.session.merge(teacher)
        self.session.commit()
        return teacher

    def delete_teacher(self, teacher: Teacher):
        self.session.delete(teacher)
        self.session.commit()
