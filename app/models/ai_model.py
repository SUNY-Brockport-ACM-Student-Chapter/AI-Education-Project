# models/ai_model.py

"""
This module contains the AI model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Ai(Base):
    """
    Represents an AI assessment of a student's answer.

    Attributes:
        ai_id (int): Primary key, auto-incrementing identifier
        assessment_text (str): AI's assessment of the answer, max 255 characters
        student_answer_id (int): Foreign key referencing the student's answer
        grade (str): AI-assigned grade (single character)
    """

    __tablename__ = "ai"

    ai_id = Column(Integer, primary_key=True, autoincrement=True)
    assessment_text = Column(String(255))
    student_answer_id = Column(Integer, ForeignKey("student_answer.student_answer_id"))
    grade = Column(String(1))

    # Add relationship
    student_answer = relationship("StudentAnswer", back_populates="ai_assessment")

    def __repr__(self):
        return f"<Ai(assessment_text={self.assessment_text}, student_answer_id={self.student_answer_id})>"
