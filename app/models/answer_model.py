# models/answer_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Answer(Base):
    """
    Represents a predefined answer for a question.

    Attributes:
        answer_id (int): Primary key, auto-incrementing identifier
        answer_text (str): The answer text, max 255 characters
        question_id (int): Foreign key referencing the question this answer belongs to
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "answer"

    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    answer_text = Column(String(255), nullable=False)
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Answer(answer_text='{self.answer_text}')>"
