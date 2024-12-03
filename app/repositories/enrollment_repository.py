# repositories/enrollment_repository.py

from sqlalchemy.orm import Session

from app.models.enrollment_model import Enrollment


class EnrollmentRepository:
    def __init__(self, session: Session):
        self.session = session

    ### status	ENUM(‘enrolled’, ‘cancelled’, ‘padding’)
    def change_enrollment_status_for_student(self, student_id: int, course_id: int, status: str):
        self.session.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).update({"status": status})
        self.session.commit()
        return self.session.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()

    def create_enrollment(self, student_id: int, course_id: int):
        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        self.session.add(new_enrollment)
        self.session.commit()
        return new_enrollment

