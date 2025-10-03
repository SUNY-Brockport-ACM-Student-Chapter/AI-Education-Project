# services/submission_service.py

from app.models.submission_model import Submission # Assuming this model exists
from app.repositories.submission_repository import SubmissionRepository # Assuming this repository exists
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class SubmissionService:
    def __init__(self, submission_repo: SubmissionRepository):
        self.submission_repo = submission_repo

    def create_submission(self, student_id: ID_TYPE, assessment_id: ID_TYPE, data: dict) -> Submission:
        """
        Creates a new submission record for a student on a specific assessment.
        """
        return self.submission_repo.create_submission(student_id, assessment_id, data)

    def get_submission_by_id(self, submission_id: ID_TYPE) -> Optional[Submission]:
        """
        Retrieves a single submission by its ID.
        """
        return self.submission_repo.get_submission_by_id(submission_id)

    def update_submission(self, submission_id: ID_TYPE, updates: dict) -> Optional[Submission]:
        """
        Updates an existing submission by its ID.
        """
        return self.submission_repo.update_submission(submission_id, updates)

    def delete_submission(self, submission_id: ID_TYPE) -> bool:
        """
        Deletes a submission by its ID.
        """
        return self.submission_repo.delete_submission(submission_id)

    def get_submissions_for_student(self, student_id: ID_TYPE) -> List[Submission]:
        """
        Retrieves all submissions made by a specific student.
        """
        return self.submission_repo.get_submissions_for_student(student_id)

    def get_submissions_for_assessment(self, assessment_id: ID_TYPE) -> List[Submission]:
        """
        Retrieves all submissions for a specific assessment.
        """
        return self.submission_repo.get_submissions_for_assessment(assessment_id)

    def mark_submission_complete(self, submission_id: ID_TYPE) -> Submission:
        """
        Marks a submission as complete and potentially calculates the final score.
        """
        return self.submission_repo.mark_submission_complete(submission_id)
