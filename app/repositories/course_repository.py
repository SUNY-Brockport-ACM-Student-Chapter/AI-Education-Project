# repositories/course_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.teacher_model import Teacher
from app.models.student_model import Student

class CourseRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_active_courses_for_teacher(self, teacher_id: int):
        teacher = self.session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
        if not teacher:
            raise ValueError("Teacher not found")
        return self.session.query(Course).filter(Course.teacher_id == teacher_id, Course.is_active == True).order_by(Course.course_code).all()
    
    def create_course(self, teacher_id: int, course_data: dict):
        teacher = self.session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
        if not teacher:
            raise ValueError("Teacher not found")
        new_course = Course(teacher_id=teacher_id, is_active = True, **course_data)
        self.session.add(new_course)
        self.session.commit()
        return new_course
    
    def update_course(self, course_id: int, course_data: dict):
        course = self.session.query(Course).filter(Course.course_id == course_id).first()
        if not course:
            raise ValueError("Course not found")
        for key, value in course_data.items():
            setattr(course, key, value)
        self.session.commit()
        return course
    
    def change_course_status(self, course_id: int):
        course = self.session.query(Course).filter(Course.course_id == course_id).first()
        if not course:
            raise ValueError("Course not found")
        if course.is_active == True:
            course.is_active = False
        else:
            course.is_active = True
        self.session.commit()
        return course
    
    def get_active_courses_for_student(self, student_id: int):
        student = self.session.query(Student).filter(Student.student_id == student_id).first()
        if not student:
            raise ValueError("Student not found")
        courses = self.session.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id, Course.is_active == True).order_by(Course.course_code).all()
        return courses
