# models/feedback_model.py
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Feedback(Base):
    """
    Represents feedback given on a submission or a specific answer.

    Attributes:
        feedback_id (str): Primary key, unique identifier.
        channel (Enum): The channel where the feedback was left.
        visibility (Enum): The visibility of the feedback (e.g., 'public', 'private').
        body (str): The content of the feedback.
        author_id (str): Foreign key to the user who left the feedback (nullable).
        submission_id (str): Foreign key to the submission the feedback is on (nullable).
        answer_id (str): Foreign key to the specific answer the feedback is on (nullable).
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
    """

    __tablename__ = "feedback"

    feedback_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    channel = Column(Enum("human", "ai", name="feedback_channel_enum"), nullable=False)
    visibility = Column(Enum("private", "public", name="visibility_enum"), nullable=False)
    body = Column(String, nullable=False)
    author_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=True) #ID_REFERENCE
    submission_id = Column(UUID(as_uuid=True), ForeignKey("submission.submission_id"), nullable=True) #ID_REFERENCE
    answer_id = Column(UUID(as_uuid=True), ForeignKey("submission_answer.submission_answer_id"), nullable=True) #ID_REFERENCE
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    author = relationship("User", back_populates="feedbacks")
    answer = relationship("SubmissionAnswer", back_populates="feedback")
    file_objects = relationship("FileObject", back_populates="feedback")

    def __repr__(self):
        return f"<Feedback(id='{self.feedback_id}', author_id='{self.author_id}')>"

    def to_dict(self):
        return {
            "feedback_id": self.feedback_id,
            "channel": self.channel,
            "visibility": self.visibility,
            "body": self.body,
            "author_id": self.author_id,
            "submission_id": self.submission_id,
            "answer_id": self.answer_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
