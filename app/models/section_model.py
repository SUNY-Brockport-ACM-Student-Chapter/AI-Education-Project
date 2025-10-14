# models/section_model.py

from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Section(Base):
    """
    Represents a specific offering of a course, e.g., "Fall 2023, Section 01".

    Attributes:
        section_id (str): Primary key, a unique identifier for the section.
        course_id (str): Foreign key referencing the course this section belongs to.
        name (str): The name or title of the section (e.g., "Section 01").
        term (str): The academic term (e.g., "Fall 2023").
        start_at (datetime): The start date and time for the section.
        end_at (datetime): The end date and time for the section.
        is_active (bool): Flag indicating if the section is currently active.
        capacity (int): The maximum number of students that can enroll.
        instructor_id (str): Foreign key referencing the instructor for this section.
        created_at (datetime): Timestamp for when the record was created.
        updated_at (datetime): Timestamp for the last update.
        deleted_at (datetime): Timestamp for when the record was soft-deleted.
    """

    __tablename__ = "section"

    section_id = Column(UUID(as_uuid=True), primary_key=True) # ID_REFERENCE
    course_id = Column(UUID(as_uuid=True), ForeignKey("course.course_id"), nullable=False) #ID_REFERENCE
    name = Column(String, nullable=False)
    term = Column(String, nullable=False)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    is_active = Column(Boolean, default=True)
    capacity = Column(Integer, default=0)
    instructor_id = Column(UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False) #ID_REFERENCE
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc)) 
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    deleted_at = Column(DateTime)

    # Relationships
    course = relationship("Course", back_populates="sections")
    instructor = relationship("User", back_populates="sections_taught")
    enrollments = relationship("Enrollment", back_populates="section")
    announcements = relationship("Announcement", back_populates="section")
    assessments = relationship("Assessment", back_populates="section")
    file_objects = relationship("FileObject", back_populates="section")

    def __repr__(self):
        return f"<Section(name='{self.name}', term='{self.term}')>"

    def to_dict(self):
        return {
            "section_id": self.section_id,
            "name": self.name,
            "course_id": self.course_id,
            "term": self.term,
            "instructor_id": self.instructor_id
        } 
