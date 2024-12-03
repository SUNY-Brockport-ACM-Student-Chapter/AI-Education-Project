# repositories/course_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.student_model import Student
from app.models.exam_model import Exam

class CourseRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_active_courses_for_teacher(self, teacher_id: int):
        return self.session.query(Course).filter(Course.teacher_id == teacher_id, Course.status == "active").order_by(Course.course_code).all()

    def create_course(self, teacher_id: int, course_data: dict):
        new_course = Course(teacher_id=teacher_id, **course_data)
        self.session.add(new_course)
        self.session.commit()
        return new_course
    
    def update_course(self, course_id: int, course_data: dict):
        self.session.query(Course).filter(Course.id == course_id).update(course_data)
        self.session.commit()
        return self.session.query(Course).filter(Course.id == course_id).first()
    
    def change_course_status(self, course_id: int, course_data: dict):
        self.session.query(Course).filter(Course.id == course_id).update(course_data)
        self.session.commit()
        return self.session.query(Course).filter(Course.id == course_id).first()
    
    def get_active_courses_for_student(self, student_id: int):
        return self.session.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id, Course.status == "active").order_by(Course.course_code).all()
