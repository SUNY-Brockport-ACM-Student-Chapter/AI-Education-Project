# models/submission_model.py
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database import Base


class Submission(Base):
    """
    Represents a student's submission for an assessment.

    Attributes:
        submission_id (str): Primary key, unique identifier for the submission.
        assessment_id (str): Foreign key linking to the assessment.
        user_id (str): Foreign key linking to the student user.
        attempt_number (int): The attempt number for this submission.
        status (enum): The current status of the submission.
        submitted_at (datetime): The time of submission.
        graded_at (datetime): The time of grading.
        grader_id (str): Foreign key linking to the grader user.
        score (float): The final score for the submission.
        late_penalty (float): The late penalty applied to the score.
        final (bool): Indicates if this is the final attempt.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
        deleted_at (datetime): Timestamp of deletion.
    """

    __tablename__ = "submission"

    submission_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    assessment_id = Column(UUID(as_uuid=True), ForeignKey("assessment.assessment_id"), nullable=False) #ID_REFERENCE
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False) #ID_REFERENCE
    attempt_number = Column(Integer, nullable=False, default=1)
    status = Column(Enum("draft", "submitted", "graded", "retracted", name="submission_status_enum"), nullable=False, default="submitted")
    submitted_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=True)
    graded_at = Column(DateTime, nullable=True)
    grader_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=True) #ID_REFERENCE
    score = Column(Float, nullable=True)
    late_penalty = Column(Float, nullable=True)
    final = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    # Relationships
    assessment = relationship("Assessment", back_populates="submissions")
    user = relationship("User", foreign_keys=[user_id], back_populates="submissions")
    grader = relationship("User", foreign_keys=[grader_id], back_populates="graded_submissions")
    rubric_scores = relationship("RubricScore", back_populates="submission")

    def __repr__(self):
        return f"<Submission(submission_id='{self.submission_id}', user_id='{self.user_id}', assessment_id='{self.assessment_id}')>"

    def to_dict(self):
        return {
            "submission_id": self.submission_id,
            "assessment_id": self.assessment_id,
            "user_id": self.user_id,
            "attempt_number": self.attempt_number,
            "status": self.status,
            "submitted_at": self.submitted_at.isoformat() if self.submitted_at else None,
            "graded_at": self.graded_at.isoformat() if self.graded_at else None,
            "grader_id": self.grader_id,
            "score": self.score,
            "late_penalty": self.late_penalty,
            "final": self.final,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }
