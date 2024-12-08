# services/enrollment_service.py

from app.models.enrollment_model import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository


class EnrollmentService:
    def __init__(self, enrollment_repo: EnrollmentRepository):
        self.enrollment_repo = enrollment_repo

    def change_enrollment_status_for_student(
        self, student_id: int, course_id: int, status: str
    ):
        return self.enrollment_repo.change_enrollment_status_for_student(
            student_id, course_id, status
        )

    def create_enrollment(self, student_id: int, course_id: int):
        return self.enrollment_repo.create_enrollment(student_id, course_id)
