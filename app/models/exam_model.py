# models/exam_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


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

    __tablename__ = "exam"

    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)
    exam_name = Column(String(100), nullable=False)
    exam_description = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    course = relationship("Course", back_populates="exams")
    questions = relationship(
        "Question", back_populates="exam", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Exam(exam_name='{self.exam_name}')>"

    def to_dict(self):
        """Convert Exam object to dictionary for JSON serialization"""
        return {
            "id": self.exam_id,
            "course_id": self.course_id,
            "name": self.exam_name,
            "description": self.exam_description,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
