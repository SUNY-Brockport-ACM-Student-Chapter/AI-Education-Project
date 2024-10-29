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

    course_id = Column(String(8), primary_key=True)
    course_name = Column(String(50), nullable=False)
    course_code = Column(String(12), nullable=False)
    course_description = Column(String(255))
    capacity = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    is_active = Column(Boolean, default=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Course(course_name='{self.course_name}')>"
