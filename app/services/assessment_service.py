# services/assessment_service.py

from app.models.assessment_model import Assessment
from app.repositories.assessment_repository import AssessmentRepository
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str

class AssessmentService:
    def __init__(self, assessment_repo: AssessmentRepository):
        self.assessment_repo = assessment_repo

    def get_assessment_by_id(self, assessment_id: ID_TYPE) -> Optional[Assessment]:
        """Retrieves a single assessment by its ID."""
        return self.assessment_repo.get_assessment_by_id(assessment_id)

    def update_assessment(self, assessment_id: ID_TYPE, data: dict) -> Assessment:
        """Updates an existing assessment by its ID."""
        return self.assessment_repo.update_assessment(assessment_id, data)

    def delete_assessment(self, assessment_id: ID_TYPE) -> bool:
        """Deletes an assessment by its ID."""
        return self.assessment_repo.delete_assessment(assessment_id)

    def get_assessments_for_teacher(self, teacher_id: ID_TYPE) -> List[Assessment]:
        """Retrieves assessments for a specific teacher."""
        return self.assessment_repo.get_assessments_for_teacher(teacher_id)

    def get_assessments_for_course(self, course_id: ID_TYPE) -> List[Assessment]:
        """Retrieves assessments for a specific course."""
        return self.assessment_repo.get_assessments_for_course(course_id)

    def create_assessment(self, course_id: ID_TYPE, data: dict) -> Assessment:
        """Creates a new assessment associated with a course."""
        return self.assessment_repo.create_assessment(course_id, data)

    def get_student_assessment_submission_stage(self, assessment_id: ID_TYPE, student_id: ID_TYPE) -> str:
        """Gets the submission stage for a student on an assessment."""
        return self.assessment_repo.get_student_assessment_submission_stage(assessment_id, student_id)

    def get_assessments_for_student(self, student_id: ID_TYPE) -> List[Assessment]:
        """Retrieves assessments assigned to a specific student."""
        return self.assessment_repo.get_assessments_for_student(student_id)
