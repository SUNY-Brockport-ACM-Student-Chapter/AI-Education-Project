# services/enrollment_service.py

from app.models.enrollment_model import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository


class EnrollmentService:
    def __init__(self, enrollment_repo: EnrollmentRepository):
        self.enrollment_repo = enrollment_repo

    def get_enrollment_by_id(self, enrollment_id: int):
        return self.enrollment_repo.get_enrollment_by_id(enrollment_id)

    def get_all_enrollments(self):
        return self.enrollment_repo.get_all_enrollments()

    def create_enrollment(self, enrollment: Enrollment):
        return self.enrollment_repo.create_enrollment(enrollment)

    def update_enrollment(self, enrollment: Enrollment):
        return self.enrollment_repo.update_enrollment(enrollment)

    def delete_enrollment(self, enrollment: Enrollment):
        return self.enrollment_repo.delete_enrollment(enrollment)
