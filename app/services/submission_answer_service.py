# services/submission_answer_service.py
from app.models.submission_answer_model import SubmissionAnswer
from app.repositories.submission_answer_repository import SubmissionAnswerRepository
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class SubmissionAnswerService:
    def __init__(self, submission_answer_repo: SubmissionAnswerRepository):
        # Renamed local variable for consistency
        self.submission_answer_repo = submission_answer_repo

    def get_submission_answer(self, answer_id: ID_TYPE) -> Optional[SubmissionAnswer]:
        """Retrieves a single submission answer by its ID."""
        return self.submission_answer_repo.get_submission_answer_by_id(answer_id)
    
    def delete_submission_answer(self, answer_id: ID_TYPE) -> bool:
        """Deletes a single submission answer by its ID."""
        return self.submission_answer_repo.delete_submission_answer(answer_id)
        
    def get_submission_answers_filtered(self, student_id: Optional[ID_TYPE] = None, question_id: Optional[ID_TYPE] = None) -> List[SubmissionAnswer]:
        """
        Retrieves submission answers filtered by optional student_id and question_id.
        Replaces the hard-coded 'get_student_answers_for_student' for flexibility.
        """
        return self.submission_answer_repo.get_submission_answers_filtered(
            student_id=student_id, 
            question_id=question_id
        )

    def create_submission_answer(self, data: dict) -> SubmissionAnswer:
        """
        Creates a new submission answer. Assumes necessary data is within the 'data' dictionary.
        """
        # The repository method must be updated to accept just the data dict
        return self.submission_answer_repo.create_submission_answer(data)

    def update_submission_answer(self, answer_id: ID_TYPE, updates: dict) -> SubmissionAnswer:
        """
        Update a submission answer.
        """
        # Ensuring consistency in variable names (updates vs data)
        updated = self.submission_answer_repo.update_submission_answer(answer_id, updates)
        return updated
