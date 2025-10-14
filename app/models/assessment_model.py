# models/exam_model.py

from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Assessment(Base):
    """
    Represents an assessment (e.g., a quiz, exam, or assignment).

    Attributes:
        assessment_id (str): Primary key, unique identifier for the assessment.
        section_id (str): Foreign key linking to the course section.
        type (str): The type of assessment (e.g., 'quiz', 'assignment', 'exam').
        name (str): The name of the assessment.
        description (str): A detailed description of the assessment.
        points (int): The total points available for the assessment.
        start_at (datetime): The date and time the assessment becomes available.
        end_at (datetime): The date and time the assessment is no longer available.
        due_at (datetime): The due date and time for the assessment.
        time_limit_minutes (int): The time limit in minutes (for timed assessments).
        max_attempts (int): The maximum number of submission attempts allowed.
        allow_late (bool): Flag to allow late submissions.
        published (bool): Flag indicating if the assessment is published for students.
        order_index (int): The display order of the assessment within a section.
        rubric_id (str): Foreign key linking to a rubric for grading.
        created_at (datetime): Timestamp for when the record was created.
        updated_at (datetime): Timestamp for the last update.
        deleted_at (datetime): Timestamp for when the record was soft-deleted.
    """

    __tablename__ = "assessment"

    assessment_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    section_id = Column(UUID(as_uuid=True), ForeignKey("section.section_id"), nullable=False) #ID_REFERENCE
    assessment_type = Column(Enum("assignment", "exam", "quiz", "project", name="assessment_type_enum"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    points = Column(Integer)
    start_at = Column(DateTime)
    end_at = Column(DateTime)
    due_at = Column(DateTime)
    time_limit_minutes = Column(Integer)
    max_attempts = Column(Integer, default=1)
    allow_late = Column(Boolean, default=False)
    published = Column(Boolean, default=False)
    order_index = Column(Integer)
    rubric_id = Column(UUID(as_uuid=True), ForeignKey("rubric.rubric_id")) #ID_REFERENCE
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    deleted_at = Column(DateTime)

    # Relationships
    section = relationship("Section", back_populates="assessments")
    rubric = relationship("Rubric", back_populates="assessments")
    questions = relationship("Question", back_populates="assessment")
    submissions = relationship("Submission", back_populates="assessment")
    ai_interactions = relationship("AIInteraction", back_populates="assessment")
    file_objects = relationship("FileObject", back_populates="assessment")

    def __repr__(self):
        return f"<Assessment(name='{self.name}', type='{self.type}')>"

    def to_dict(self):
        return {
            "assessment_id": self.assessment_id,
            "section_id": self.section_id,
            "name": self.name,
            "type": self.type,
            "points": self.points,
            "start_at": self.start_at.isoformat() if self.start_at else None,
            "due_at": self.due_at.isoformat() if self.due_at else None,
            "published": self.published
        }
