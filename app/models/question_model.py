# models/question_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


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

    __tablename__ = "question"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey("exam.exam_id"), nullable=False)
    question_text = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    exam = relationship("Exam", back_populates="questions")
    student_answers = relationship(
        "StudentAnswer", back_populates="question", cascade="all, delete-orphan"
    )
    answers = relationship(
        "Answer", back_populates="question", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Question(question_id={self.question_id})>"
