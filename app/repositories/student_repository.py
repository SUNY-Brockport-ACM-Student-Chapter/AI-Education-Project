# repositories/student_repository.py

from sqlalchemy.orm import Session

from app.models.student_model import Student


class StudentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_student_by_id(self, student_id: int):
        return self.session.query(Student).filter(Student.id == student_id).first()

    def get_all_students(self):
        return self.session.query(Student).all()

    def create_student(self, student: Student):
        self.session.add(student)
        self.session.commit()
        return student

    def update_student(self, student: Student):
        self.session.merge(student)
        self.session.commit()
        return student

    def delete_student(self, student: Student):
        self.session.delete(student)
        self.session.commit()
