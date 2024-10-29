# models/studentAnswer_model.py

from datetime import datetime, timezone
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


class StudentAnswer(Base):
    """
    Represents a student's answer to an exam question.

    Attributes:
        student_answer_id (int): Primary key, auto-incrementing identifier
        student_id (int): Foreign key referencing the student
        question_id (int): Foreign key referencing the question
        answer_text (str): Student's answer text, max 255 characters
        second_attempt_answer (str): Second attempt answer text, defaults to first answer
        answer_grade (str): Grade for first attempt (single character)
        second_attempt_grade (str): Grade for second attempt, defaults to first grade
        answer_stage (int): Indicates the current attempt stage (1 or 2)
        created_at (datetime): Timestamp when the answer was created
        updated_at (datetime): Timestamp when the answer was last updated
    """

    __tablename__ = "student_answer"

    student_answer_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    answer_text = Column(String(255))
    second_attempt_answer = Column(String(255), default=answer_text)
    answer_grade = Column(String(1), nullable=False)
    second_attempt_grade = Column(String(1), default=answer_grade)
    answer_stage = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # Add the relationship to Ai
    ai_assessment = relationship("Ai", back_populates="student_answer", uselist=False)

    def __repr__(self):
        return f"<StudentAnswer(student_id = {self.student_id}, question_id = {self.question_id})>"
