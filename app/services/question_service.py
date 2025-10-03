# services/question_service.py

from app.models.question_model import Question
from app.repositories.question_repository import QuestionRepository
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str

class QuestionService:
    def __init__(self, question_repo: QuestionRepository):
        self.question_repo = question_repo

    def create_question(self, assignment_id: ID_TYPE, data: dict) -> Question:
        """
        Creates a new question associated with a specific assignment.
        """
        # Renamed argument from assessment_id to assignment_id
        return self.question_repo.create_question(assignment_id, data)

    def get_questions_for_assignment(self, assignment_id: ID_TYPE) -> List[Question]:
        """
        Retrieves all questions for a given assignment ID.
        """
        # Renamed method/repo call from assessment to assignment
        return self.question_repo.get_questions_for_assignment(assignment_id)

    def get_question_by_id(self, question_id: ID_TYPE) -> Optional[Question]:
        """
        Retrieves a single question by its ID.
        """
        return self.question_repo.get_question_by_id(question_id)

    def update_question(self, question_id: ID_TYPE, data: dict) -> Optional[Question]:
        """
        Updates an existing question by its ID.
        """
        return self.question_repo.update_question(question_id, data)
        
    def delete_question(self, question_id: ID_TYPE) -> bool:
        """
        Deletes a question by its ID.
        """
        return self.question_repo.delete_question(question_id)
