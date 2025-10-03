# repositories/ai_repository.py
import uuid
from sqlalchemy.orm import Session
from app.models.ai_interaction_model import AIInteraction
from app.models.submission_model import Submission # Only imported for validation/clarity


class AIInteractionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_ai_feedback_for_submission(self, submission_id: uuid.UUID): # Renamed method
        """Retrieves the AIInteraction (e.g., feedback) for a specific Submission."""
        
        # NOTE: You're checking for Submission existence here, which is fine, 
        # but the query for AIInteraction is what is actually returned.
        submission = ( # Renamed variable
            self.session.query(Submission)
            .filter(Submission.submission_id == submission_id)
            .first()
        )
        if not submission:
            raise ValueError("Submission not found") # Corrected error message

        ai_assessment = ( # Corrected typo
            self.session.query(AIInteraction)
            .filter(AIInteraction.submission_id == submission_id)
            .order_by(AIInteraction.created_at.desc()) # Order by latest interaction
            .first()
        )
        return ai_assessment