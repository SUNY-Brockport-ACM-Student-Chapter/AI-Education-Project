# models/exam_model.py

from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from database import Base


class Exam(Base):
    """
    Represents an exam in the system.

    Attributes:
        exam_id (int): Primary key, auto-incrementing identifier
        course_id (int): Foreign key referencing the course this exam belongs to
        exam_name (str): Name of the exam, max 100 characters
        exam_description (str): Description of the exam content, max 255 characters
        start_date (datetime): When the exam becomes available
        end_date (datetime): When the exam closes
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "exams"

    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"), nullable=False)
    exam_name = Column(String(100), nullable=False)
    exam_description = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    def __repr__(self):
        return f"<Exam(exam_name='{self.exam_name}')>"