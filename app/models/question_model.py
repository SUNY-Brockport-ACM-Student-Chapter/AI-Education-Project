# models/question_model.py
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Question(Base):
    """
    Represents a question within an assessment.

    Attributes:
        question_id (str): Primary key, unique identifier.
        assessment_id (str): Foreign key linking to the parent assessment.
        kind (Enum): The type of question (e.g., 'multiple_choice', 'essay').
        text (str): The body of the question.
        points (int): The points this question is worth (nullable).
        order_index (int): The display order of the question within the assessment (nullable).
        config (JSON): JSON configuration for the question (e.g., choices for multiple choice).
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
        deleted_at (datetime): Timestamp of deletion.
    """

    __tablename__ = "question"

    question_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("assessment.assessment_id"), nullable=False) #ID_REFERENCE
    kind = Column(Enum("mcq", "multi_select", "true_false", "fib", "short", "long", "code", name="question_kind_enum"), nullable=False)
    text = Column(String, nullable=False)
    points = Column(Integer)
    order_index = Column(Integer)
    config = Column(JSON)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    deleted_at = Column(DateTime)

    # Relationships
    assessment = relationship("Assessment", back_populates="questions")
    answers = relationship("SubmissionAnswer", back_populates="question")

    def __repr__(self):
        return f"<Question(id='{self.question_id}', kind='{self.kind}')>"

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "assessment_id": self.assessment_id,
            "kind": self.kind,
            "text": self.text,
            "points": self.points,
            "order_index": self.order_index,
            "config": self.config,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }
