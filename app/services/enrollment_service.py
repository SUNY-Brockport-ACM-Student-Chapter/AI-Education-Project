# services/enrollment_service.py

from app.models.enrollment_model import Enrollment
from app.repositories.enrollment_repository import EnrollmentRepository
from typing import Optional

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class EnrollmentService:
    def __init__(self, enrollment_repo: EnrollmentRepository):
        self.enrollment_repo = enrollment_repo

    def get_enrollment_by_id(self, enrollment_id: ID_TYPE) -> Optional[Enrollment]:
        """Retrieves a single enrollment record by its ID."""
        return self.enrollment_repo.get_enrollment_by_id(enrollment_id)
        
    def update_enrollment(self, enrollment_id: ID_TYPE, updates: dict) -> Enrollment:
        """Updates an existing enrollment record."""
        return self.enrollment_repo.update_enrollment(enrollment_id, updates)
        
    def delete_enrollment(self, enrollment_id: ID_TYPE) -> bool:
        """Deletes a single enrollment record by its ID."""
        return self.enrollment_repo.delete_enrollment(enrollment_id)

    def change_enrollment_status_for_student(
        self, student_id: ID_TYPE, course_id: ID_TYPE, status: str
    ) -> Enrollment:
        """Changes the status of a student's enrollment in a course."""
        return self.enrollment_repo.change_enrollment_status_for_student(
            student_id, course_id, status
        )

    def create_enrollment(self, student_id: ID_TYPE, course_id: ID_TYPE) -> Enrollment:
        """Creates a new enrollment record."""
        return self.enrollment_repo.create_enrollment(student_id, course_id)
