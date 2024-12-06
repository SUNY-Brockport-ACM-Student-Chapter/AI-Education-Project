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

    def search_for_students(self, data: dict):
        if not data:
            raise ValueError("Search query is required")
        search_query = ""
        if data.get("user_name"):
            search_query += data.get("user_name")
        if data.get("first_name"):
            search_query += data.get("first_name")
        if data.get("last_name"):
            search_query += data.get("last_name")
        if data.get("email"):
            search_query += data.get("email")
        students = self.session.query(Student).filter(Student.name.ilike(f"%{search_query}%")).all()
        if not students:
            raise ValueError("No students found")
        return students
    
    def get_students_for_course(self, course_id: int):
        return self.session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()
    