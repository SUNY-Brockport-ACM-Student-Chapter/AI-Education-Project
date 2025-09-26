# models/submission_answer_model.py
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class SubmissionAnswer(Base):
    """
    Represents a single answer within a submission.

    Attributes:
        submission_answer_id (str): Primary key, unique identifier for the answer.
        submission_id (str): Foreign key linking to the parent submission.
        question_id (str): Foreign key linking to the specific question.
        response (JSON): The student's response to the question.
        auto_score (float): Automatically generated score (nullable).
        is_correct (bool): Indicates if the auto-score determined the answer is correct (nullable).
        manual_score (float): Manually entered score by a grader (nullable).
        comment (str): Optional comments from the grader (nullable).
        ai_feedback (str): Feedback provided by an AI (nullable).
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
    """

    __tablename__ = "submission_answer"

    submission_answer_id = Column(String(12), primary_key=True) #ID_REFERENCE
    submission_id = Column(String(12), ForeignKey("submission.submission_id"), nullable=False) #ID_REFERENCE
    question_id = Column(String(12), ForeignKey("question.question_id"), nullable=False) #ID_REFERENCE
    response = Column(String)  # Using String for simplicity, can be more specific like JSON or JSONB
    auto_score = Column(Float)
    is_correct = Column(Boolean)
    manual_score = Column(Float)
    comment = Column(String)
    ai_feedback = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    submission = relationship("Submission", back_populates="answers")
    question = relationship("Question", back_populates="answers")

    def __repr__(self):
        return f"<SubmissionAnswer(id='{self.submission_answer_id}', submission_id='{self.submission_id}')>"

    def to_dict(self):
        return {
            "submission_answer_id": self.submission_answer_id,
            "submission_id": self.submission_id,
            "question_id": self.question_id,
            "response": self.response,
            "auto_score": self.auto_score,
            "is_correct": self.is_correct,
            "manual_score": self.manual_score,
            "comment": self.comment,
            "ai_feedback": self.ai_feedback,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
