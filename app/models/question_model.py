# models/question_model.py

from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from database import Base


class Question(Base):
    """
    Represents a question within an exam.

    Attributes:
        question_id (int): Primary key, auto-incrementing identifier
        exam_id (int): Foreign key referencing the exam this question belongs to
        question_text (str): The actual question text, max 255 characters
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey("exams.exam_id"), nullable=False)
    question_text = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    def __repr__(self):
        return f"<Question(question_text='{self.question_text}')>"
