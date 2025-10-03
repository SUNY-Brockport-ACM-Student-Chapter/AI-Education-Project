# models/enrollment_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class Rubric(Base):
    """
    Represents a grading rubric for an assessment.

    Attributes:
        rubric_id (str): Primary key, unique identifier for the rubric.
        title (str): The title of the rubric.
        description (str): A detailed description of the rubric.
        created_at (datetime): Timestamp for when the record was created.
        updated_at (datetime): Timestamp for the last update.
    """

    __tablename__ = "rubric"

    rubric_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    title = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # Relationships
    assessments = relationship("Assessment", back_populates="rubric")

    def __repr__(self):
        return f"<Rubric(title='{self.title}')>"

    def to_dict(self):
        return {
            "rubric_id": self.rubric_id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
