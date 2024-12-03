# repositories/student_repository.py

from sqlalchemy.orm import Session

from app.models.student_model import Student
from app.models.course_model import Course
from app.models.exam_model import Exam
from app.models.teacher_model import Teacher
from app.models.enrollment_model import Enrollment

class StudentRepository:
    def __init__(self, session: Session):
        self.session = session

    def search_for_students(self, search_query: str):
        return self.session.query(Student).filter(Student.name.ilike(f"%{search_query}%")).all()
    
    def get_students_for_course(self, course_id: int):
        return self.session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()
    