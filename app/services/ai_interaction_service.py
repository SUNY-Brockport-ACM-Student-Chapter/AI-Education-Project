# services/ai_interaction_service.py

"""
This module contains the service for the AI Interaction model.
"""

from app.repositories.ai_interaction_repository import AIInteractionRepository
from app.models.ai_interaction_model import AIInteraction
from typing import Optional

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class AIInteractionService:
    def __init__(self, ai_interaction_repo: AIInteractionRepository):
        # Renamed local variable for consistency
        self.ai_interaction_repo = ai_interaction_repo
        
    def create_interaction(self, data: dict) -> AIInteraction:
        """Creates a new AI interaction record (POST /ai-interaction)."""
        return self.ai_interaction_repo.create_interaction(data)
        
    def get_interaction_by_id(self, interaction_id: ID_TYPE) -> Optional[AIInteraction]:
        """Retrieves a single AI interaction by its ID (GET /ai-interaction/{id})."""
        return self.ai_interaction_repo.get_interaction_by_id(interaction_id)
        
    def update_interaction(self, interaction_id: ID_TYPE, data: dict) -> AIInteraction:
        """Updates an existing AI interaction by its ID (PATCH /ai-interaction/{id})."""
        return self.ai_interaction_repo.update_interaction(interaction_id, data)
        
    def delete_interaction(self, interaction_id: ID_TYPE) -> bool:
        """Deletes an AI interaction by its ID (DELETE /ai-interaction/{id})."""
        return self.ai_interaction_repo.delete_interaction(interaction_id)

    def get_ai_assessment_for_submission_answer(self, submission_answer_id: ID_TYPE) -> Optional[AIInteraction]:
        """
        Retrieves the AI assessment/feedback associated with a specific SubmissionAnswer ID.
        Renamed method from get_ai_assesment_for_studentAnswer.
        """
        return self.ai_interaction_repo.get_ai_assessment_for_submission_answer(submission_answer_id)
        
    def get_ai_assessment_for_submission(self, submission_id: ID_TYPE) -> Optional[AIInteraction]:
        """
        Retrieves the AI assessment/feedback associated with a specific Submission ID.
        This supports the new route: /ai-interaction/submission/<submission_id>
        """
        return self.ai_interaction_repo.get_ai_assessment_for_submission(submission_id)
