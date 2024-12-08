# repositories/enrollment_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.student_model import Student


class EnrollmentRepository:
    def __init__(self, session: Session):
        self.session = session

    ### status	ENUM(‘enrolled’, ‘cancelled’, ‘padding’)
    def change_enrollment_status_for_student(
        self, student_id: int, course_id: int, status: str
    ):
        student = (
            self.session.query(Student).filter(Student.student_id == student_id).first()
        )
        if not student:
            raise ValueError("Student not found")
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")

        enrollment = (
            self.session.query(Enrollment)
            .filter(
                Enrollment.student_id == student_id, Enrollment.course_id == course_id
            )
            .first()
        )
        if not enrollment:
            raise ValueError("Enrollment not found")
        enrollment.status = status
        self.session.commit()
        return enrollment

    def create_enrollment(self, student_id: int, course_id: int):
        student = (
            self.session.query(Student).filter(Student.student_id == student_id).first()
        )
        if not student:
            raise ValueError("Student not found")
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")
        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        self.session.add(new_enrollment)
        self.session.commit()
        return new_enrollment
