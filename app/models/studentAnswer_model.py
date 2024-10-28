# models/studentAnswer_model.py

import datetime
from datetime import UTC, datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from database import Base


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
    """

    __tablename__ = "student answer"

    student_answer_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey=("students.student_id"), nullable=False)
    question_id = Column(Integer, ForeignKey=("questions.question_id"), nullable=False)
    answer_text = Column(String(255))
    second_attempt_answer = Column(String(255), default=answer_text)
    answer_grade = Column(String(1), nullable=False)
    second_attempt_grade = Column(String(1), default=answer_grade)
    answer_stage = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<StudentAnswer(student_id = {self.student_id}, question_id = {self.question_id})>"
