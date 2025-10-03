# models/ai_interaction_model.py
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class AIInteraction(Base):
    """
    Logs interactions with AI models.

    Attributes:
        ai_interaction_id (str): Primary key, unique identifier.
        user_id (str): Foreign key to the user who initiated the interaction (nullable).
        assessment_id (str): Foreign key to the assessment related to the interaction (nullable).
        submission_id (str): Foreign key to the submission related to the interaction (nullable).
        purpose (str): The purpose of the interaction.
        model (str): The name of the AI model used.
        prompt_tokens (int): The number of tokens in the prompt.
        completion_tokens (int): The number of tokens in the completion.
        latency_ms (int): The latency of the interaction in milliseconds.
        ai_interaction_metadata (JSON): Additional ai_interaction_metadata about the interaction.
        created_at (datetime): Timestamp of creation.
    """

    __tablename__ = "ai_interaction"

    ai_interaction_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=True) #ID_REFERENCE
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("assessment.assessment_id"), nullable=True) #ID_REFERENCE
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submission.submission_id"), nullable=True) #ID_REFERENCE
    purpose = Column(String, nullable=False)
    model = Column(String, nullable=False)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    latency_ms = Column(Integer)
    ai_interaction_metadata = Column(JSON)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    user = relationship("User", back_populates="ai_interactions")
    assessment = relationship("Assessment", back_populates="ai_interactions")
    submission = relationship("Submission", back_populates="ai_interactions")

    def __repr__(self):
        return f"<AIInteraction(id='{self.ai_interaction_id}', user_id='{self.user_id}', purpose='{self.purpose}')>"

    def to_dict(self):
        return {
            "ai_interaction_id": self.ai_interaction_id,
            "user_id": self.user_id,
            "assessment_id": self.assessment_id,
            "submission_id": self.submission_id,
            "purpose": self.purpose,
            "model": self.model,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "latency_ms": self.latency_ms,
            "ai_interaction_metadata": self.ai_interaction_metadata,
            "created_at": self.created_at.isoformat(),
        }
