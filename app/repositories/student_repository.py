# repositories/student_repository.py

from models.student_model import Student
from sqlalchemy.orm import Session
import datetime

class StudentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_student_by_id(self, student_id: int):
        return self.session.query(Student).filter(Student.student_id == student_id).first()

    def get_all_students(self):
        return self.session.query(Student).all()

    def create_student(self, user_name: str, first_name: str, last_name: str, email: str, clerk_user_id: str):
        student = Student(
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            email=email,
            clerk_user_id=clerk_user_id,
            last_login=datetime.utcnow(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(student)
        self.session.commit()
        return student

    def update_student(self, student_id: int, **kwargs):
        student = self.get_student_by_id(student_id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)
            self.session.commit()
        return student

    def delete_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        if student:
            self.session.delete(student)
            self.session.commit()
        return student
