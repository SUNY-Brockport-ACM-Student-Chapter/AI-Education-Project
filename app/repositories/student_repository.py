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

    def get_student_by_id(self, student_id: int):
        return (
            self.session.query(Student).filter(Student.student_id == student_id).first()
        )

    def get_student_by_clerk_user_id(self, clerk_user_id: str):
        return (
            self.session.query(Student).filter(Student.clerk_user_id == clerk_user_id).first()
        )

    def get_all_courses_for_student(self, student_id: int):
        enrollments = self.session.query(Enrollment).filter(Enrollment.student_id == student_id).all()
        courses = self.session.query(Course).filter(Course.course_id.in_(enrollment.course_id for enrollment in enrollments)).all()
        return courses

    def get_all_exams_for_student(self, student_id: int):
        courses = self.get_all_courses_for_student(student_id)
        exams = self.session.query(Exam).filter(Exam.course_id.in_(course.course_id for course in courses)).all()
        return exams

    
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

    def get_student_by_clerk_id(self, clerk_user_id: str):
        return (
            self.session.query(Student)
            .filter(Student.clerk_user_id == clerk_user_id)
            .first()
        )
