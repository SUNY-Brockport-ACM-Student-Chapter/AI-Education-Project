# repositories/enrollment_repository.py

from sqlalchemy.orm import Session

from app.models.enrollment_model import Enrollment


class EnrollmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_enrollment_by_id(self, enrollment_id: int):
        return (
            self.session.query(Enrollment)
            .filter(Enrollment.id == enrollment_id)
            .first()
        )

    def get_all_enrollments(self):
        return self.session.query(Enrollment).all()

    def create_enrollment(self, enrollment: Enrollment):
        self.session.add(enrollment)
        self.session.commit()
        return enrollment

    def update_enrollment(self, enrollment: Enrollment):
        self.session.merge(enrollment)
        self.session.commit()
        return enrollment

    def delete_enrollment(self, enrollment: Enrollment):
        self.session.delete(enrollment)
        self.session.commit()
