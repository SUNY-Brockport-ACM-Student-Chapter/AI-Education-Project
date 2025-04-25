# models/course_model.py

from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Course(Base):
    """
    Represents a course in the system.

    Attributes:
        course_id (str): Primary key, 8-character course identifier
        course_name (str): Name of the course, max 50 characters
        course_code (str): Course code (e.g., CS101), max 12 characters
        course_description (str): Description of the course, max 255 characters
        capacity (int): Maximum number of students allowed
        teacher_id (int): Foreign key referencing the teacher
        is_active (bool): Whether the course is currently active
        start_date (datetime): When the course begins
        end_date (datetime): When the course ends
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "course"

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(50), nullable=False)
    course_code = Column(String(12), nullable=False)
    course_description = Column(String(255))
    capacity = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))  # fks
    is_active = Column(Boolean, default=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Add relationship to Teacher
    teacher = relationship("Teacher", back_populates="courses")

    # Add relationship to Enrollment
    enrollment = relationship("Enrollment", back_populates="course")

    # Add relationship to Exam
    exams = relationship("Exam", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Course(course_name='{self.course_name}')>"

    def to_dict(self):
        """Convert Course object to dictionary for JSON serialization"""
        return {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "course_description": self.course_description,
            "capacity": self.capacity,
            "teacher_id": self.teacher_id,
            "is_active": self.is_active,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
        }
